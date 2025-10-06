# # agent.py
# from google.adk.tools.google_search_tool import GoogleSearchTool
# from google.adk.agents import Agent

# # 1. Instantiate the GoogleSearch tool
# google_search_tool = GoogleSearchTool()

# # 2. Define the agent
# search_agent = Agent(
#     name="search_agent",
#     model="gemini-2.0-flash",
#     instruction=(
#         "You are an expert at answering user queries by performing Google searches. Search should restrict to www.att.com and its sub domains only "
#         "Use the Google Search tool to find relevant information and provide a concise summary."
#         "Unsupported queries should handover back to parent agent"
#     ),
#     tools=[google_search_tool]
# )