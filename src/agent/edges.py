from src.agent.state import FinancialAgentState

def route_advisor_flow(state: FinancialAgentState) -> str:
    # Conditional edge: check if human verification is required
    if state.get("needs_approval", False):
        return "human_approval"
    return "end"
