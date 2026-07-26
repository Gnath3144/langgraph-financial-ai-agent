from typing import Sequence, List, Dict, Any
from langchain_core.messages import BaseMessage

def reduce_messages(left: Sequence[BaseMessage], right: Sequence[BaseMessage]) -> Sequence[BaseMessage]:
    # Reducer: Appends new messages to conversation state
    merged = list(left)
    for msg in right:
        if msg not in merged:
            merged.append(msg)
    return merged

def reduce_profile(left: Dict[str, Any], right: Dict[str, Any]) -> Dict[str, Any]:
    # Reducer: Merges updates into user profiles
    new_profile = dict(left) if left else {}
    if right:
        new_profile.update(right)
    return new_profile

def reduce_goals(left: List[str], right: List[str]) -> List[str]:
    # Reducer: Deduplicates and merges goals list
    merged = list(left) if left else []
    if right:
        for goal in right:
            if goal not in merged:
                merged.append(goal)
    return merged
