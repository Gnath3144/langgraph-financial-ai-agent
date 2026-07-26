# LangGraph Financial AI Agent

An enterprise-grade Financial Advisor Agent built using LangGraph, LangChain, SQLite persistence, and Streamlit.

## Business Problem
Providing financial or investment advice autonomously carries regulatory risks. This agent integrates **Human-in-the-Loop (HITL) interrupts**, allowing human advisors to inspect and approve/reject investment recommendations before they are executed.

## Folder Structure
```
├── assets/
├── docs/
│   └── generate_slides.py
├── demo/
│   └── app.py
├── notebooks/
│   └── hands_on_tutorial.ipynb
├── src/
│   └── agent/
│       ├── config.py
│       ├── edges.py
│       ├── graph.py
│       ├── llm.py
│       ├── main.py
│       ├── memory.py
│       ├── nodes.py
│       ├── reducers.py
│       ├── router.py
│       ├── schemas.py
│       └── tools.py
├── tests/
│   └── test_agent.py
├── Dockerfile
├── requirements.txt
└── setup.py
```

## Installation
```bash
pip install -r requirements.txt
```

## Running Locally
Start the Streamlit Demo:
```bash
streamlit run demo/app.py
```

## Run Unit Tests
```bash
python -m pytest -p no:langsmith tests
```
