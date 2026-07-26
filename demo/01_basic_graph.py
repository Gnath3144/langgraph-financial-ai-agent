# 01_basic_graph.py
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    input_text: str
    output_text: str

def process_node(state: State):
    return {"output_text": state["input_text"].upper()}

builder = StateGraph(State)
builder.add_node("process", process_node)
builder.add_edge(START, "process")
builder.add_edge("process", END)
graph = builder.compile()

res = graph.invoke({"input_text": "hello edureka"})
print("Basic Graph Result:", res)
