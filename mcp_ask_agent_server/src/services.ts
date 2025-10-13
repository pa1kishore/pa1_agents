import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import  * as tools from "./tools.js";

function additionTool(server: McpServer) {
    console.log("Registering addition tool...");
    server.tool("addition", {
            a: z.number().describe("The first number"),
            b: z.number().describe("The second number")
        },
        async ({a,b}) => {
        return {
            content:[
                {
                    type: "text",
                    text: JSON.stringify({result: await tools.addition(a,b)})
                }
            ]
        }
    });
}

function subtractionTool(server: McpServer) {
    console.log("Registering subtraction tool...");

    server.tool("subtraction", {
            a: z.number().describe("The first number"),
            b: z.number().describe("The second number")
        },
        async ({a,b}) => {
        return {
            content:[
                {
                    type: "text",
                    text: JSON.stringify({result: await tools.subtraction(a,b)})
                }
            ]
        }
    });
}

function multiplicationTool(server: McpServer) {
    console.log("Registering multiplication tool...");
    server.tool("multiplication", {
            a: z.number().describe("The first number"),
            b: z.number().describe("The second number")
        },
        async ({a,b}) => {
        return {
            content:[
                {
                    type: "text",
                    text: JSON.stringify({result: await tools.multiplication(a,b)})
                }
            ]
        }
    });
}

function divisionTool(server: McpServer) {
    console.log("Registering division tool...");

    server.tool("division", {
            a: z.number().describe("The first number"),
            b: z.number().describe("The second number")
        },
        async ({a,b}) => {
        return {
            content:[
                {
                    type: "text",
                    text: JSON.stringify({result: await tools.division(a,b)})
                }
            ]
        }
    });
}

export function registerServices(server: McpServer) {
    additionTool(server);
    subtractionTool(server);
    multiplicationTool(server);
    divisionTool(server);
}
