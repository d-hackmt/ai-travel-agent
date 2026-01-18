from langchain_tavily import TavilySearch
from src.config.config import TAVILY_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

def tavily_search_tool(query: str) -> str:
    """
    Search the web using Tavily to get up-to-date travel information,
    attractions, activities, tips, and local insights for a given query.
    """
    tavily_search = TavilySearch(
        max_results=5,
        topic="general",
        tavily_api_key=TAVILY_API_KEY
    )
    return tavily_search.invoke({"query": query})


logger.info("TAVILY TOOL ALL SET")