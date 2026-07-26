import uuid
from langchain_core.messages import HumanMessage
from src.agent.graph import build_financial_agent

class FinancialAgentRunner:
    def __init__(self):
        self.graph = build_financial_agent()

    def query(self, text: str, thread_id: str = None) -> dict:
        if not thread_id:
            thread_id = str(uuid.uuid4())
            
        config = {"configurable": {"thread_id": thread_id}}
        inputs = {
            "messages": [HumanMessage(content=text)],
            "profile": {"risk_tolerance": "moderate", "income": 8000, "expenses": 5000},
            "goals": ["Retire by 55"],
            "context": {},
            "needs_approval": False,
            "approved": False,
            "advice_output": ""
        }
        
        # Run graph
        res = self.graph.invoke(inputs, config)
        return res, thread_id

if __name__ == "__main__":
    runner = FinancialAgentRunner()
    res, tid = runner.query("I want to invest $15000 in apple stock. What is your advice?")
    print("Agent Output:", res.get("advice_output", ""))
    print("Is interrupt active (needs approval)?", res.get("needs_approval", False))
