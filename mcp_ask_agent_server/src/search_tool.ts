import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
// import fetch from "node-fetch";

let search_api_host = process.env.SEARCH_API_HOST || "https://services.att.com";
// Product types optional filter
const getSearchData = async (query: string, productTypes: string[]): Promise<any> => {
    // Simulate a search operation (replace with actual search logic)
    console.log(`Searching for "${query}" in product types: ${productTypes.join(', ')}`);
    let url = `${search_api_host}/search/v1/topdocs?app-id=sitesearch&rows=7&fl=chatURL,los,chunk_html,chunk_markdown,title&q=${encodeURIComponent(query)}`
    // if (productTypes.length > 0) {
    //     url += `&fq=productType:(${productTypes.map(pt => `"${pt}"`).join(' OR ')})`;
    // }
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Search API request failed with status ${response.status}`);
    }
    const data = await response.json();
    let finalDocs=[];
    if (data.response && data.response.docs) {
        finalDocs = data.response.docs.map((doc: any) => ({
            title: doc.title,
            url: doc.chatURL,
            los: doc.los,
            content: doc.chunk_markdown || doc.chunk_html
        }));
    }
    console.log(`Search API response: ${JSON.stringify(finalDocs)}`);
    return finalDocs;
}

const getSearchDataTool = (server: McpServer) => {
    console.log("Registering search tool...");

    server.registerTool("search", {
            title: "Search Tool",
            description: "Search for documents from the knowledge base.",
            inputSchema: {
                query: z.string().describe("The search query"),
                productTypes: z.array(z.string()).describe("The product types to filter by (optional)").optional().default([])
            },
            
        },
        async ({query, productTypes}) => {
        return {
            content:[
                {
                    type: "text",
                    text: JSON.stringify({result: await getSearchData(query, productTypes)}) // Return search results as JSON string
                }
            ]
        };
    });
}

export default getSearchDataTool;