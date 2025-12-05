from google.adk.agents import Agent
from ask_agent_mcp.tools.sqlite_mcp import get_sqlite_toolset
class SqlAgentApp(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="sql_agent",
            model="gemini-2.5-flash",
            instruction="""
                You are a helpful Virtual assistant agent. You can manage and interact with customer information stored in a SQLite database.
                Customer information related information (store, retrieve, modify, delete) stored in SQLite database. Customer information includes customer, customer plans, plans etc...
                You can interact tools relalted to SQLite databases to respond to user queries.""",
            # tools=[AgentTool(SupportQnAAgent())],
            **kwargs
        )
        mcp_tools = get_sqlite_toolset()
        self.tools.extend(mcp_tools) 


    # def __init__(self):
    #     # 1. Create the agent instance first
    #     sql_agent_instance = self._create_sql_agent()
    #     self.agent = sql_agent_instance
    #     # 2. Pass the created instance to the superclass
    #     super().__init__(agent=self.agent)

    # def _create_sql_agent(self) -> Agent:
    #     mcp_tools = get_sqlite_toolset()
    #     agent = Agent(
    #         model="gemini-2.5-flash",
    #         name="sql_agent",
    #         instruction="""
    #             You are a helpful Virtual assistant agent. You can manage and interact with customer information stored in a SQLite database.
    #             Customer information related information (store, retrieve, modify, delete) stored in SQLite database. Customer information includes customer, customer plans, plans etc...
    #             You can interact tools relalted to SQLite databases to respond to user queries.""",
    #         tools=[mcp_tools]
    #     )
    #     return agent