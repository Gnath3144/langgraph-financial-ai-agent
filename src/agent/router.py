from langchain_core.messages import AIMessage
from src.agent.state import FinancialAgentState

def route_intent(state: FinancialAgentState) -> str:
    # Router logic: inspects last message for routing
    if not state["messages"]:
        return "general"
        
    last_msg = state["messages"][-1].content.lower()
    if "invest" in last_msg or "advice" in last_msg or "stock" in last_msg or "budget" in last_msg:
        return "financial"
    return "general"
