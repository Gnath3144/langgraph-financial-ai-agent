from langchain_core.messages import AIMessage
from src.agent.state import FinancialAgentState
from src.agent.llm import get_chat_model

llm = get_chat_model()

def general_chat_node(state: FinancialAgentState):
    # Node: Standard chit chat handler
    response = llm.invoke(state["messages"])
    return {
        "messages": [response],
        "advice_output": response.content,
        "needs_approval": False
    }

def financial_advisor_node(state: FinancialAgentState):
    # Node: Analytical financial profiling advisor
    response = llm.invoke(state["messages"])
    # Determine if investment advice requires human signoff (> $10k or general recommendation)
    needs_approval = "approve" in response.content.lower() or "signoff" in response.content.lower()
    return {
        "messages": [response],
        "advice_output": response.content,
        "needs_approval": needs_approval,
        "approved": False
    }

def human_approval_node(state: FinancialAgentState):
    # Node: Human-in-the-Loop decision gate. It will suspend execution.
    if state.get("approved", False):
        msg = AIMessage(content="Advisor: Investment proposal approved and executed.")
    else:
        msg = AIMessage(content="Advisor: Investment proposal rejected by adviser.")
        
    return {
        "messages": [msg],
        "advice_output": msg.content,
        "needs_approval": False
    }
