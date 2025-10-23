import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import  * as tools from "./tools.js";

function additionTool(server: McpServer) {
    console.log("Registering addition tool...");
    server.registerTool("addition", {
            title: "Addition Tool",
            description: "Add two numbers",
            inputSchema: {
                a: z.number().describe("The first number"),
                b: z.number().describe("The second number")
            },
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

    server.registerTool("subtraction", {
            title: "Subtraction Tool",
            description: "Subtract two numbers",
            inputSchema: {
                a: z.number().describe("The first number"),
                b: z.number().describe("The second number")
            },
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
    server.registerTool("multiplication", {
            title: "Multiplication Tool",
            description: "Multiply two numbers",
            inputSchema: {
                a: z.number().describe("The first number"),
                b: z.number().describe("The second number")
            },
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

    server.registerTool("division", {
            title: "Division Tool",
            description: "Divide two numbers",
            inputSchema: {
                a: z.number().describe("The first number"),
                b: z.number().describe("The second number")
            },
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
