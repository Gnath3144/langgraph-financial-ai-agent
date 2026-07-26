from langgraph.graph import StateGraph, START, END
from src.agent.state import FinancialAgentState
from src.agent.nodes import general_chat_node, financial_advisor_node, human_approval_node
from src.agent.edges import route_advisor_flow
from src.agent.router import route_intent
from src.agent.memory import get_sqlite_checkpointer

def build_financial_agent():
    # Assembles StateGraph
    builder = StateGraph(FinancialAgentState)
    
    # Add Nodes
    builder.add_node("general_chat", general_chat_node)
    builder.add_node("financial_advisor", financial_advisor_node)
    builder.add_node("human_approval", human_approval_node)
    
    # Define START routes
    builder.add_conditional_edges(
        START,
        route_intent,
        {
            "general": "general_chat",
            "financial": "financial_advisor"
        }
    )
    
    # General chat goes directly to END
    builder.add_edge("general_chat", END)
    
    # Financial advisor conditional route
    builder.add_conditional_edges(
        "financial_advisor",
        route_advisor_flow,
        {
            "human_approval": "human_approval",
            "end": END
        }
    )
    
    builder.add_edge("human_approval", END)
    
    # Setup Checkpointer Memory & Compile Graph
    memory = get_sqlite_checkpointer()
    
    # Compile with human interrupt before the approval node!
    compiled_graph = builder.compile(
        checkpointer=memory,
        interrupt_before=["human_approval"]
    )
    
    return compiled_graph
