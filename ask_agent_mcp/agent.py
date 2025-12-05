import os
import pathlib
import json

from google.adk.agents import Agent, BaseAgent
from vertexai.agent_engines import AdkApp
from ask_agent_mcp.sqlite_agent import SqlAgentApp
from ask_agent_mcp.tools.mcp_server import get_mcp_toolset
class UberAgentApp(AdkApp):
    def __init__(self):
        # 1. Create the agent instance first
        uber_agent_instance = self._create_uber_agent()
        self.agent = uber_agent_instance
        # 2. Pass the created instance to the superclass
        super().__init__(agent=self.agent)

    def _create_uber_agent(self) -> Agent:
        mcp_tools = get_mcp_toolset()
        agent = Agent(
            model="gemini-2.5-flash",
            name="ask_agent_mcp",
            instruction="""
                You are a helpful AT&T Virtual assistant agent that can interact with various agents and tools and responds to user queries.
                Delegate SqlAgentApp for any Customer information related information (store, retrieve, modify, delete) stored in SQLite database. Customer information includes customer, customer plans, plans etc...""",
            tools=[mcp_tools],
            sub_agents=[SqlAgentApp()]
        )
        return agent

# root_agent = UberAgent()
adk_app = UberAgentApp()
root_agent: BaseAgent = adk_app.agent