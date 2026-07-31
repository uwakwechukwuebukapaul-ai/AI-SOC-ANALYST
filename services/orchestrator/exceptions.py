"""
Sentinel DNA
Enterprise Investigation Orchestrator Exceptions

Defines custom exception types used throughout the
Investigation Orchestrator.

Author: Sentinel DNA
"""


class OrchestratorError(Exception):
    """
    Base exception for all orchestrator-related errors.
    """

    def __init__(self, message="An orchestrator error occurred."):
        super().__init__(message)


class WorkflowError(OrchestratorError):
    """
    Raised when a workflow execution fails.
    """

    def __init__(self, message="Workflow execution failed."):
        super().__init__(message)


class InvalidStateTransitionError(WorkflowError):
    """
    Raised when an invalid state transition is attempted.
    """

    def __init__(self, current_state, requested_state):
        message = (
            f"Invalid state transition "
            f"from '{current_state}' "
            f"to '{requested_state}'."
        )
        super().__init__(message)


class InvestigationValidationError(OrchestratorError):
    """
    Raised when an investigation context fails validation.
    """

    def __init__(self, message="Investigation validation failed."):
        super().__init__(message)


class PipelineExecutionError(OrchestratorError):
    """
    Raised when a pipeline stage cannot complete.
    """

    def __init__(self, stage, reason):
        message = (
            f"Pipeline stage '{stage}' failed: {reason}"
        )
        super().__init__(message)


class ServiceIntegrationError(OrchestratorError):
    """
    Raised when an external or internal service integration fails.
    """

    def __init__(self, service_name, reason):
        message = (
            f"Service '{service_name}' failed: {reason}"
        )
        super().__init__(message)


class PersistenceError(OrchestratorError):
    """
    Raised when database persistence fails.
    """

    def __init__(self, message="Failed to persist investigation data."):
        super().__init__(message)


class ThreatIntelligenceError(OrchestratorError):
    """
    Raised when threat intelligence enrichment fails.
    """

    def __init__(self, provider, reason):
        message = (
            f"Threat intelligence provider "
            f"'{provider}' failed: {reason}"
        )
        super().__init__(message)