# 04_tools_demo.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.agent.tools import get_mock_stock_price, calculate_compound_interest

print("AAPL Stock Price:", get_mock_stock_price.invoke("AAPL"))
print("Compound Interest:", calculate_compound_interest.invoke({"principal": 10000, "rate": 5, "years": 10}))
