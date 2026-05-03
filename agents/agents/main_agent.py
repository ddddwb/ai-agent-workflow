class MainAgent:
    def __init__(self):
        pass

    def plan_task(self, user_input: str):
        return {
            "goal": user_input,
            "steps": [
                "analyze",
                "execute",
                "validate",
                "refine"
            ]
        }

    def run(self, user_input: str):
        plan = self.plan_task(user_input)

        result = []
        for step in plan["steps"]:
            result.append(f"[Agent] {step} done")

        return "\n".join(result)
