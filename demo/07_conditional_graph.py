# 07_conditional_graph.py
import sys, types
m = types.ModuleType('uuid_utils'); m.compat = types.ModuleType('uuid_utils.compat'); m.compat.uuid7 = lambda: __import__('uuid').uuid4(); sys.modules['uuid_utils'] = m; sys.modules['uuid_utils.compat'] = m.compat

from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    number: int
    result: str

def classifier_node(state: State):
    return {}

def even_node(state: State):
    return {"result": f"{state['number']} is EVEN"}

def odd_node(state: State):
    return {"result": f"{state['number']} is ODD"}

def is_even_or_odd(state: State) -> str:
    if state["number"] % 2 == 0:
        return "even"
    return "odd"

builder = StateGraph(State)
builder.add_node("classifier", classifier_node)
builder.add_node("even", even_node)
builder.add_node("odd", odd_node)

builder.add_conditional_edges(
    "classifier",
    is_even_or_odd,
    {
        "even": "even",
        "odd": "odd"
    }
)

builder.add_edge(START, "classifier")
builder.add_edge("even", END)
builder.add_edge("odd", END)
graph = builder.compile()

res_even = graph.invoke({"number": 42})
print("Result for 42:", res_even["result"])
res_odd = graph.invoke({"number": 7})
print("Result for 7:", res_odd["result"])
