# 06_finance_agent.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.agent.main import FinancialAgentRunner

runner = FinancialAgentRunner()
res, tid = runner.query("I want to invest $15000 in apple stock. What is your advice?")
print("Agent Output:", res.get("advice_output", ""))
print("State Next Steps:", runner.graph.get_state({"configurable": {"thread_id": tid}}).next)
