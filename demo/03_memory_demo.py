# 03_memory_demo.py
import sys, types
m = types.ModuleType('uuid_utils'); m.compat = types.ModuleType('uuid_utils.compat'); m.compat.uuid7 = lambda: None; sys.modules['uuid_utils'] = m; sys.modules['uuid_utils.compat'] = m.compat

import sqlite3
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, List

class State(TypedDict):
    history: List[str]

def add_message(state: State):
    return {"history": ["Step logged"]}

builder = StateGraph(State)
builder.add_node("add", add_message)
builder.add_edge(START, "add")
builder.add_edge("add", END)

conn = sqlite3.connect(":memory:", check_same_thread=False)
memory = SqliteSaver(conn)
graph = builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "session-1"}}
res1 = graph.invoke({"history": ["Init"]}, config)
print("Run 1 State:", graph.get_state(config).values)
res2 = graph.invoke(None, config)
print("Run 2 State (Checkpoint retrieved):", graph.get_state(config).values)
