from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from src.tools.tavily_tool import tavily_search_tool
from src.tools.serper_tool import google_serper_search_tool
from src.config.config import GROQ_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

model = init_chat_model(
    model="groq:llama-3.3-70b-versatile",
    temperature=0.3
)

SYSTEM_PROMPT = """
You are an expert AI travel planner.

Rules:
- Always use web search tools for real-world accuracy
- Create a detailed day-wise itinerary
- Include food suggestions, local tips, and travel advice

User Inputs:
City, Number of days, Interests, Travel style, Pace
"""

agent = create_agent(
    model=model,
    tools=[tavily_search_tool, google_serper_search_tool],
    system_prompt=SYSTEM_PROMPT.strip()
)

logger.info("AGENT SUCCESSFULLY CREATED")
