import os
import pathlib
import json
from .prompts.prompts import UBER_AGENT_PROMPT
from google.adk.agents import Agent, BaseAgent
from vertexai.agent_engines import AdkApp
from ask_agent_classes.constants import DEFAULT_MODEL
from .support_master_agent import SupportMasterAgent

def create_mcp_toolset():
    from google.adk.tools.mcp_tool.mcp_toolset import (
        MCPToolset,
        StreamableHTTPConnectionParams,
    )


    # Your Cloud Run URL for the MCP Toolbox

    # MCP_SERVER_URL = os.environ.get("MCP_SERVER_URL")

    MCP_SERVER_URL = os.environ.get("MCP_SERVER_URL", "https://mcp-ask-agent-server-908887859066.us-east4.run.app/mcp")

    # Configure the MCPToolset to connect to the remote server
    mcp_tools = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=MCP_SERVER_URL
        ),
        errlog=None
    )
    return mcp_tools


class UberAgentApp(AdkApp):
    def __init__(self):
        # 1. Create the agent instance first
        uber_agent_instance = self._create_uber_agent()
        self.agent = uber_agent_instance
        # 2. Pass the created instance to the superclass
        super().__init__(agent=self.agent)

    def _create_uber_agent(self) -> Agent:
        mcp_tools = create_mcp_toolset()
        agent = Agent(
            model=DEFAULT_MODEL,
            name="ask_agent_classes",
            instruction=UBER_AGENT_PROMPT,
            sub_agents=[SupportMasterAgent(mcp_tools=mcp_tools)],
            tools=[mcp_tools]
        )
        return agent

# root_agent = UberAgent()
adk_app = UberAgentApp()
root_agent: BaseAgent = adk_app.agent