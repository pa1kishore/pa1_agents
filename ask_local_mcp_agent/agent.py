from google.adk.agents import Agent
from .prompts import MASTER_AGENT_MCP, MASTER_AGENT
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from pathlib import Path


PATH_TO_YOUR_MCP_SERVER_SCRIPT = str((Path(__file__).parent / "tools" / "mcp_server.py").resolve())

# 2. Define the agent

root_agent = Agent(
    name="ask_local_mcp_agent",
    model="gemini-2.0-flash",
    instruction=MASTER_AGENT_MCP,
    tools=[
            MCPToolset(
            connection_params=StdioServerParameters(
                command="python3",
                args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT],
            )
        )
    ]
)

