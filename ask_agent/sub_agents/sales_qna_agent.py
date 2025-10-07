# agent.py
from ask_agent.tools.tool_rag_query import tool_rag_query
from google.adk.agents import Agent
import os
RAG_CORPUS_NAME = os.getenv("RAG_CORPUS_NAME")
# 1. Instantiate the GoogleSearch tool


# 2. Define the agent
sales_qna_agent = Agent(
    name="sales_qna_agent",
    model="gemini-2.0-flash",
    instruction=(
        "You are an expert at answering user queries related to Sales or upgrade."
        f"Use alawys \"{RAG_CORPUS_NAME}\" as corpus_name "
        "Use tool_rag_query to get required contextual data from AT&T portal and then generate response based on contextual data"
        "Use tool_rag_query only if tool context doesnt have required information to fullfil user query"
    ),
    tools=[tool_rag_query]
)