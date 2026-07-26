# 05_human_in_loop.py
import sqlite3
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict

class State(TypedDict):
    needs_review: bool
    approved: bool

def process_advice(state: State):
    return {"needs_review": True}

def execution_node(state: State):
    print("Executing investment transaction...")
    return {"needs_review": False}

builder = StateGraph(State)
builder.add_node("advice", process_advice)
builder.add_node("execution", execution_node)
builder.add_edge(START, "advice")
builder.add_edge("advice", "execution")
builder.add_edge("execution", END)

conn = sqlite3.connect(":memory:", check_same_thread=False)
memory = SqliteSaver(conn)

graph = builder.compile(checkpointer=memory, interrupt_before=["execution"])

config = {"configurable": {"thread_id": "tx-1"}}
res = graph.invoke({"needs_review": False, "approved": False}, config)
print("State suspended. Next node to run:", graph.get_state(config).next)

graph.update_state(config, {"approved": True}, as_node="advice")
res_final = graph.invoke(None, config)
print("Finished. Final State values:", graph.get_state(config).values)
