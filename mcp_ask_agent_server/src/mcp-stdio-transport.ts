import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const startStdioTransport = async (server: McpServer) => {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.log("MCP Server is running and connected via stdio transport.");

};
export { startStdioTransport };