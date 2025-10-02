# agent.py
# from google.adk.agents import LlmAgent
from google.adk.agents import Agent
from .sub_agents.weather_agent import weather_agent
from .sub_agents.search_agent import search_agent
# 2. Define the agent
root_agent = Agent(
    name="ask_agent",
    model="gemini-2.0-flash",
    instruction=(
        "You are an expert at answering user queries"
        "use weather_agent for Weather and time for any city"
        "Use search_agent all the generic user queries."
    ),
    sub_agents=[weather_agent, search_agent]
)