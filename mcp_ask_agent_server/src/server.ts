import { McpServer, ResourceTemplate } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import express from 'express';

import { registerServices } from './services';
import { randomUUID } from 'node:crypto';
import { startStdioTransport } from './mcp-stdio-transport';
import getSearchDataTool from './search_tool';

// Create an MCP server
const server = new McpServer({
    name: 'mcp_ask_agent_server',
    version: '1.0.0'
});

registerServices(server)

getSearchDataTool(server);

const transport = new StreamableHTTPServerTransport({
            sessionIdGenerator: undefined,
            enableJsonResponse: true
        });


// Set up Express and HTTP transport
const app = express();
// app.use(express.raw());
app.get('/', (req, res) => {
    res.send('Hello! This is the MCP server. Use the /mcp endpoint for MCP requests.');
});
app.get('/health', (req, res) => {
    res.send('OK');
});
app.post('/mcp', async (req, res) => {
    const requestId = randomUUID();
    
    console.log(`[${requestId}] Received request to /mcp`);
    
    try {
        
        // Pass the raw body (a Buffer) to the transport
        await transport.handleRequest(req, res, req.body);
        console.log(`[${requestId}] Response sent for /mcp`);
    } catch (e) {
        console.error(`[${requestId}] Error handling request:`, e);
        res.status(500).json({
            jsonrpc: '2.0',
            error: { code: -32603, message: 'Internal server error', data: e.message },
            id: null
        });
    }

});

const port = parseInt(process.env.PORT || '8080');
// Use an async function to ensure proper startup sequence
async function startServer() {
    try {
        // 4. Await the connection to ensure it's complete
        await server.connect(transport);
        
        // 5. Only start listening for requests after connection is successful
        app.listen(port, () => {
            console.log(`Demo MCP Server running on http://localhost:${port}/mcp`);
        });
    } catch (error) {
        console.error('Server failed to start:', error);
        process.exit(1);
    }
}

// Call the async startup function
startServer();

// startStdioTransport(server);