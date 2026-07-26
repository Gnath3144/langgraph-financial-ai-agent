# Standalone basic flow
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List

class SimpleState(TypedDict):
    val: str

def add_node(state: SimpleState):
    return {"val": state["val"] + " -> Hello"}

builder = StateGraph(SimpleState)
builder.add_node("adder", add_node)
builder.add_edge(START, "adder")
builder.add_edge("adder", END)
graph = builder.compile()

res = graph.invoke({"val": "Input"})
print("Result:", res["val"])
