"""
Sentinel DNA Agent Pipeline

Canonical investigation execution adapter.

The pipeline translates an ExecutionPlan into runtime task
execution while keeping orchestration separate from runtime
scheduling and execution.

Architecture
------------
InvestigationCoordinator
    -> AgentPipeline
    -> Runtime Task
    -> RuntimeTaskExecutor
    -> Agent capability
    -> BaseAgent.execute()

The pipeline does not own scheduling, retry policy, metrics,
resource management, or runtime lifecycle.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.orchestration.orchestration_result import (
    OrchestrationResult,
)
from services.intelligence.runtime.task import Task


class AgentPipeline:
    """
    Canonical investigation execution adapter.

    Responsibilities
    -----------------
    - resolve investigation agents
    - translate agents into runtime capabilities
    - create runtime Tasks
    - submit tasks through the configured runtime boundary
    - normalize execution results into OrchestrationResult

    Non-responsibilities
    --------------------
    - scheduling
    - worker management
    - retries
    - runtime metrics
    - resource allocation
    - policy enforcement
    - agent lifecycle management

    A registry is retained for backward compatibility with existing
    orchestration tests and legacy callers.
    """

    def __init__(
        self,
        registry: Any,
        runtime: Any | None = None,
    ) -> None:
        self.registry = registry
        self.runtime = runtime

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    def execute(
        self,
        plan: Any,
        context: Any,
    ) -> OrchestrationResult:
        """
        Execute all agents declared by an ExecutionPlan.

        Runtime-aware execution is preferred when a runtime is
        configured.

        The legacy registry path remains available when no runtime
        is supplied.
        """

        output = OrchestrationResult(
            plan_name=plan.name,
        )

        for agent_name in plan.agents:
            try:
                result = self._execute_agent(
                    agent_name=agent_name,
                    context=context,
                )

                if result is None:
                    output.add_error(
                        f"Agent not found: {agent_name}"
                    )
                    continue

                output.add_agent_result(
                    agent_name,
                    result,
                )

            except Exception as error:
                output.add_error(
                    f"{agent_name}: {error}"
                )

        return output

    # ------------------------------------------------------------------
    # Agent resolution / execution boundary
    # ------------------------------------------------------------------

    def _execute_agent(
        self,
        agent_name: str,
        context: Any,
    ) -> Any:
        """
        Execute an individual investigation agent.

        Runtime execution is preferred.

        The registry fallback remains temporarily for compatibility
        with legacy callers and existing orchestration tests.
        """

        agent = self._resolve_agent(
            agent_name
        )

        if agent is None:
            return None

        if self.runtime is not None:
            return self._execute_runtime_agent(
                agent_name=agent_name,
                agent=agent,
                context=context,
            )

        return self._execute_legacy_agent(
            agent_name=agent_name,
            agent=agent,
            context=context,
        )

    # ------------------------------------------------------------------
    # Agent resolution
    # ------------------------------------------------------------------

    def _resolve_agent(
        self,
        agent_name: str,
    ) -> Any | None:
        """
        Resolve an agent from the compatibility registry.

        Registry implementations may expose get(), resolve(), or
        dictionary-style lookup.
        """

        get = getattr(
            self.registry,
            "get",
            None,
        )

        if callable(get):
            return get(agent_name)

        resolve = getattr(
            self.registry,
            "resolve",
            None,
        )

        if callable(resolve):
            return resolve(agent_name)

        if isinstance(
            self.registry,
            dict,
        ):
            return self.registry.get(
                agent_name
            )

        raise TypeError(
            "Configured agent registry does not expose "
            "get(), resolve(), or dictionary lookup."
        )

    # ------------------------------------------------------------------
    # Legacy execution
    # ------------------------------------------------------------------

    def _execute_legacy_agent(
        self,
        agent_name: str,
        agent: Any,
        context: Any,
    ) -> Any:
        """
        Execute an agent directly through the legacy registry path.
        """

        execute = getattr(
            agent,
            "execute",
            None,
        )

        if not callable(execute):
            raise TypeError(
                f"Agent '{agent_name}' does not expose "
                "a callable execute() method."
            )

        return execute(
            context
        )

    # ------------------------------------------------------------------
    # Runtime execution
    # ------------------------------------------------------------------

    def _execute_runtime_agent(
        self,
        agent_name: str,
        agent: Any,
        context: Any,
    ) -> Any:
        """
        Execute an agent through the canonical runtime boundary.

        The preferred runtime contract is:

            runtime.submit(task)
            runtime.next_task()
            runtime executor executes the task

        Direct runtime execute interfaces are retained as
        compatibility paths for partially migrated runtime
        implementations.
        """

        capability = self._resolve_capability(
            agent_name=agent_name,
            agent=agent,
        )

        task = Task(
            capability=capability,
            payload={
                "context": context,
            },
            metadata={
                "agent_name": agent_name,
                "execution_source": "agent_pipeline",
            },
        )

        # --------------------------------------------------------------
        # Canonical RuntimeTaskExecutor-style boundary
        # --------------------------------------------------------------

        task_executor = getattr(
            self.runtime,
            "task_executor",
            None,
        )

        if task_executor is not None:
            execute = getattr(
                task_executor,
                "execute",
                None,
            )

            if callable(execute):
                return self._unwrap_runtime_result(
                    execute(task)
                )

        # --------------------------------------------------------------
        # Runtime engine boundary
        # --------------------------------------------------------------

        execute = getattr(
            self.runtime,
            "execute",
            None,
        )

        if callable(execute):
            return self._execute_runtime_engine(
                execute=execute,
                task=task,
                agent=agent,
            )

        # --------------------------------------------------------------
        # Runtime route compatibility
        # --------------------------------------------------------------

        route = getattr(
            self.runtime,
            "route",
            None,
        )

        if callable(route):
            return route(
                capability,
                context,
            )

        raise TypeError(
            "Configured runtime does not expose a supported "
            "task_executor, execute(), or route() interface."
        )

    # ------------------------------------------------------------------
    # Runtime engine adapter
    # ------------------------------------------------------------------

    def _execute_runtime_engine(
        self,
        execute: Any,
        task: Task,
        agent: Any,
    ) -> Any:
        """
        Adapt RuntimeEngine.execute(task, handler) to the agent
        execution contract.

        RuntimeEngine owns lifecycle and metrics.

        The agent remains responsible for actual intelligence work.
        """

        agent_execute = getattr(
            agent,
            "execute",
            None,
        )

        if not callable(agent_execute):
            raise TypeError(
                f"Agent '{task.metadata.get('agent_name')}' "
                "does not expose a callable execute() method."
            )

        def handler(
            runtime_task: Task,
            runtime_context: Any,
        ) -> Any:
            del runtime_context

            payload = runtime_task.payload

            context = payload.get(
                "context"
            )

            return agent_execute(
                context
            )

        result = execute(
            task,
            handler,
        )

        return self._unwrap_runtime_result(
            result
        )

    # ------------------------------------------------------------------
    # Capability resolution
    # ------------------------------------------------------------------

    def _resolve_capability(
        self,
        agent_name: str,
        agent: Any,
    ) -> str:
        """
        Resolve the runtime capability identity for an agent.

        Capability resolution order:

        1. explicit agent capability attribute
        2. first declared BaseAgent capability
        3. agent name fallback
        """

        capability = getattr(
            agent,
            "capability",
            None,
        )

        if isinstance(
            capability,
            str,
        ) and capability.strip():
            return capability

        capabilities = getattr(
            agent,
            "capabilities",
            None,
        )

        if callable(capabilities):
            capabilities = capabilities()

        if capabilities:
            first = capabilities[0]

            value = getattr(
                first,
                "value",
                None,
            )

            if isinstance(
                value,
                str,
            ) and value.strip():
                return value

            name = getattr(
                first,
                "name",
                None,
            )

            if isinstance(
                name,
                str,
            ) and name.strip():
                return name

            if isinstance(
                first,
                str,
            ) and first.strip():
                return first

        return agent_name

    # ------------------------------------------------------------------
    # Runtime result normalization
    # ------------------------------------------------------------------

    @staticmethod
    def _unwrap_runtime_result(
        result: Any,
    ) -> Any:
        """
        Normalize ExecutionResult-style runtime responses.

        Successful ExecutionResult objects expose their actual
        result through .output.

        Legacy/plain values are returned unchanged.
        """

        if result is None:
            return None

        output = getattr(
            result,
            "output",
            None,
        )

        success = getattr(
            result,
            "success",
            None,
        )

        if success is not None:
            if success:
                return output

            error = getattr(
                result,
                "error",
                None,
            )

            if error:
                raise RuntimeError(
                    str(error)
                )

            return None

        return result