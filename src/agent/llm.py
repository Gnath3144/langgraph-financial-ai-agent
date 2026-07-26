from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.outputs import ChatResult, ChatGeneration
from src.agent.config import USE_MOCK_LLM, OPENAI_API_KEY
from langchain_openai import ChatOpenAI

class MockFinancialLLM(BaseChatModel):
    def _generate(self, messages: list[BaseMessage], stop=None, run_manager=None, **kwargs):
        last_msg = messages[-1].content.lower()
        
        if "invest" in last_msg or "advice" in last_msg or "stock" in last_msg:
            content = "Based on your financial profile, I recommend a moderate diversified portfolio. Let's allocate $15,000. Under MLOps policies, this transaction requires human advisor signoff. Do you approve?"
        elif "profile" in last_msg or "income" in last_msg:
            content = "I have updated your user profile details. Your monthly surplus has been calculated."
        elif "delete" in last_msg or "clear memory" in last_msg:
            content = "Are you sure you want to clear your local memory logs? This action requires validation."
        else:
            content = "Welcome to your AI Financial Planner. I can analyze saving goals, simulate portfolios, or log budget parameters."
            
        generation = ChatGeneration(message=AIMessage(content=content))
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "mock-financial-chat"

def get_chat_model():
    if USE_MOCK_LLM or not OPENAI_API_KEY:
        return MockFinancialLLM()
    return ChatOpenAI(model="gpt-4-turbo", temperature=0)
