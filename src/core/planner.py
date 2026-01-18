from langchain_core.messages import HumanMessage, AIMessage
from src.agents.travel_agent import agent
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)


class TravelPlanner:
    def __init__(self):
        self.messages = []
        logger.info("Travel Planner initialized")

    def create_itinerary(
        self,
        city: str,
        days: int,
        interests: list[str],
        style: str,
        pace: str,
        month: str | None = None
    ):
        try:
            user_prompt = f"""
            Plan a {days}-day trip to {city}

            Interests: {', '.join(interests)}
            Travel Style: {style}
            Pace: {pace}
            Month: {month or 'Any'}

            Provide a detailed itinerary.
            """

            self.messages.append(HumanMessage(content=user_prompt))

            response = agent.invoke({
                "messages": self.messages
            })

            final_answer = response["messages"][-1].content
            self.messages.append(AIMessage(content=final_answer))

            return final_answer

        except Exception as e:
            logger.error(f"Planner error: {e}")
            raise CustomException("Failed to generate itinerary", e)
