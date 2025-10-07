# agent.py
from ask_agent.tools.tool_qna_search import tool_support_qna_search
from google.adk.agents import Agent

# 1. Instantiate the GoogleSearch tool


# 2. Define the agent
support_qna_agent = Agent(
    name="support_qna_agent",
    model="gemini-2.0-flash",
    instruction=(
        "You are an expert at answering user queries related to AT&T products and services."
        "Use tool_qna_search to get required contextual data from AT&T portal and then generate response based on contextual data"
        "Use tool_qna_search only if tool context doesnt have required information to fullfil user query"
    ),
    tools=[tool_support_qna_search]
)