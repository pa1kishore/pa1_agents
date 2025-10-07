from google.adk.agents import Agent
from .sub_agents.weather_agent import weather_agent
from .sub_agents.support_qna_agent import support_qna_agent
from .sub_agents.sales_qna_agent import sales_qna_agent
# 2. Define the agent
root_agent = Agent(
    name="ask_agent",
    model="gemini-2.0-flash",
    instruction=(
        "You are an expert at answering user queries"
        "use support_qna_agent for all non sales user queries"
        "use sales_qna_agent for any generic user queries related to sales or upgrade. Incase sales_qna_agent unable to provide required response then handover request to support_qna_agent"
        "use support_qna_agent for any generic user queries related to AT&T products and services. Also, about user accounts, billing, troubleshoot etc..."
        "use weather_agent for Weather and time for any city"
        # "Use search_agent all Non AT&T related generic user queries."
    ),
    sub_agents=[weather_agent, support_qna_agent, sales_qna_agent]
)