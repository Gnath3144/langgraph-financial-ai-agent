from pydantic import BaseModel, Field
from typing import Optional, List

class UserProfile(BaseModel):
    name: str = "Client"
    income: float = 0.0
    expenses: float = 0.0
    risk_tolerance: str = "moderate" # low, moderate, high
    cash_savings: float = 0.0
    investments: float = 0.0

class InvestmentProposal(BaseModel):
    asset_class: str
    amount: float
    reason: str

class AdviceResponse(BaseModel):
    advice: str
    requires_approval: bool = False
    proposal: Optional[InvestmentProposal] = None
