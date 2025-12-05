from google.adk.tools.mcp_tool.mcp_toolset import (
        MCPToolset,
        StreamableHTTPConnectionParams,
    )
import os
def get_mcp_toolset():
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