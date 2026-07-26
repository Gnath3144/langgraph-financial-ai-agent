import pytest
from src.agent.reducers import reduce_profile, reduce_goals
from src.agent.graph import build_financial_agent
from langchain_core.messages import HumanMessage

def test_reducers():
    # Verify profile reducer merges dicts
    p1 = {"risk_tolerance": "moderate", "income": 5000}
    p2 = {"income": 6000}
    res = reduce_profile(p1, p2)
    assert res["risk_tolerance"] == "moderate"
    assert res["income"] == 6000
    
    # Verify goals reducer deduplicates
    g1 = ["Retire by 50"]
    g2 = ["Retire by 50", "Buy house"]
    res_g = reduce_goals(g1, g2)
    assert len(res_g) == 2
    assert "Buy house" in res_g

def test_graph_interrupt():
    graph = build_financial_agent()
    config = {"configurable": {"thread_id": "test-thread"}}
    
    # Query that triggers advice and human interrupt
    inputs = {
        "messages": [HumanMessage(content="I want to invest $15000 in AAPL stock.")],
        "profile": {"risk_tolerance": "moderate"},
        "goals": []
    }
    
    res = graph.invoke(inputs, config)
    state = graph.get_state(config)
    
    # Confirm state was suspended before 'human_approval' node!
    assert state.next == ("human_approval",)
