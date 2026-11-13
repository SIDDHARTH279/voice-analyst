from langchain_core.tools import tool
from langchain_groq import ChatGroq
from src.tools.finance import get_financials as _get_financials
import os 
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    model='openai/gpt-oss-120b',
    api_key=os.getenv('GROQ_API_KEY')
)

@tool
def get_financials(ticker: str) -> dict:
    """Get key financial metrics (price, P/E, growth, margins) for a listed
    company by its stock ticker. Indian NSE stocks end with .NS, e.g. TCS.NS"""
    return _get_financials(ticker)

llm_with_tool = llm.bind_tools([get_financials])
response = llm_with_tool.invoke("What's TCS's P/E ratio?")

for call in response.tool_calls:
    result = get_financials.invoke(call["args"])
    print(result)