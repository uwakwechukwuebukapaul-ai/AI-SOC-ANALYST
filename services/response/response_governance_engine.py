"""
Sentinel DNA - Response Governance Engine

Controls and validates autonomous response actions
before execution.
"""


class ResponseGovernanceEngine:

    def __init__(self):
        self.policies = {}
        self.audit_history = []

    def register_policy(self, action, policy):

        self.policies[action] = policy

        return {
            "action": action,
            "registered": True
        }

    def check_permission(self, action, user_role):

        policy = self.policies.get(action)

        if not policy:
            return False

        allowed_roles = policy.get(
            "allowed_roles",
            []
        )

        return user_role in allowed_roles

    def requires_approval(self, action):

        policy = self.policies.get(action)

        if not policy:
            return True

        return policy.get(
            "requires_approval",
            True
        )

    def authorize_action(
        self,
        action,
        user_role,
        approved=False
    ):

        permitted = self.check_permission(
            action,
            user_role
        )

        approval_required = self.requires_approval(
            action
        )

        authorized = (
            permitted
            and (
                not approval_required
                or approved
            )
        )

        record = {
            "action": action,
            "user_role": user_role,
            "authorized": authorized
        }

        self.audit_history.append(record)

        return record

    def validate_response_plan(
        self,
        response_plan,
        user_role,
        approved=False
    ):

        results = []

        for action in response_plan.get(
            "actions",
            []
        ):

            results.append(
                self.authorize_action(
                    action,
                    user_role,
                    approved
                )
            )

        return results

    def get_audit_history(self):

        return self.audit_history

    def clear_history(self):

        self.audit_history.clear()