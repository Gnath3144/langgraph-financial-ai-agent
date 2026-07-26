# 02_state_demo.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from langgraph.graph import StateGraph, START, END
from typing import Annotated, TypedDict, Dict, Any
from src.agent.reducers import reduce_profile

class State(TypedDict):
    profile: Annotated[Dict[str, Any], reduce_profile]

def update_node(state: State):
    return {"profile": {"income": 12000}}

builder = StateGraph(State)
builder.add_node("update", update_node)
builder.add_edge(START, "update")
builder.add_edge("update", END)
graph = builder.compile()

initial_state = {"profile": {"name": "Alice", "income": 10000}}
res = graph.invoke(initial_state)
print("Updated State:", res)
