from langchain_core.tools import tool

@tool
def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculates compound interest accumulated over years at an annual interest rate."""
    return principal * ((1 + rate/100) ** years)

@tool
def analyze_monthly_budget(income: float, expenses: float) -> str:
    """Analyzes savings rate based on monthly income and expenses."""
    savings = income - expenses
    savings_rate = (savings / income) * 100 if income > 0 else 0
    if savings_rate >= 20:
        return f"Healthy budget! Savings rate is {savings_rate:.2f}%."
    return f"Savings rate is low ({savings_rate:.2f}%). Target 20% by lowering expenses."

@tool
def get_mock_stock_price(ticker: str) -> float:
    """Retrieves mock stock price for ticker."""
    ticker = ticker.upper()
    prices = {"AAPL": 185.20, "MSFT": 420.50, "GOOGL": 175.80, "NVDA": 950.00}
    return prices.get(ticker, 100.00)
