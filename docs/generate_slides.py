# Presentation slides generation helper
import os
import build_utils

slides_data = [
    {
        "title": "LangGraph Core Architecture",
        "type": "content",
        "bullets": [
            "LangGraph is an extension of LangChain designed to build cyclic state graphs.",
            "Nodes represent execution tasks (Python functions, API calls, or LLM invoke steps).",
            "Edges define state routing paths based on logic or conditions.",
            "SQLite Checkpointers store state history locally, enabling robust memory sessions."
        ],
        "notes": "Explain how LangGraph facilitates building stateful multi-agent workflows."
    },
    {
        "title": "State, Reducers, and Interventions",
        "type": "content",
        "bullets": [
            "State preserves context and parameters across nodes.",
            "Reducers merge node outputs into current state variables without overriding.",
            "Interrupts pause graph execution before specific nodes (Human-in-the-Loop approval loops)."
        ],
        "notes": "Discuss why interrupts are critical in compliance-sensitive tasks like finance or health."
    }
]

build_utils.create_presentation(
    "LangGraph Financial Agent Masterclass",
    "State management, human-in-the-loop, and SQLite checkpointer execution",
    slides_data,
    os.path.join(os.path.dirname(__file__), "presentation.pptx")
)
