from typing import Annotated, Sequence, TypedDict, Dict, Any, List
from langchain_core.messages import BaseMessage
from src.agent.reducers import reduce_messages, reduce_profile, reduce_goals

class FinancialAgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], reduce_messages]
    profile: Annotated[Dict[str, Any], reduce_profile]
    goals: Annotated[List[str], reduce_goals]
    context: Dict[str, Any]
    needs_approval: bool
    approved: bool
    advice_output: str
