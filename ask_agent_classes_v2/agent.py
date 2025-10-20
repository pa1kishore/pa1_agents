import os
import pathlib
import json
from .prompts.prompts import UBER_AGENT_PROMPT
from google.adk.agents import Agent
from ask_agent_classes_v2.constants import GEMINI_2_5_MODEL
from .support_master_agent import SupportMasterAgent
# from google.adk.tools.mcp_tool.mcp_toolset import (
#     MCPToolset,
#     StreamableHTTPConnectionParams,
# )


# # Your Cloud Run URL for the MCP Toolbox

# # MCP_SERVER_URL = os.environ.get("MCP_SERVER_URL")

# MCP_SERVER_URL = os.environ.get("MCP_SERVER_URL", "https://mcp-ask-agent-server-908887859066.us-east4.run.app/mcp")

# # Configure the MCPToolset to connect to the remote server
# mcp_tools = MCPToolset(
#     connection_params=StreamableHTTPConnectionParams(
#         url=MCP_SERVER_URL
#     )
# )


class UberAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="ask_agent_classes_v2",
            model=GEMINI_2_5_MODEL,
            instruction=UBER_AGENT_PROMPT,
            # sub_agents are passed to the super class
            # The following line assumes you have a SupportMasterAgent class
            sub_agents=[SupportMasterAgent()],
            **kwargs
        )

root_agent = UberAgent()