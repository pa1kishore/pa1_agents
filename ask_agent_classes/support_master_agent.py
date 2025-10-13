import os
import pathlib
import json
from .prompts.prompts import UBER_AGENT_PROMPT
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from ask_agent_classes.constants import GEMINI_2_5_MODEL
from typing import ClassVar
from ask_agent_classes.sub_agents.sub_agent_qna import SupportQnAAgent
from ask_agent_classes.sub_agents.sub_agent_billing import BillingGroupAgent
from ask_agent_classes.sub_agents.sub_agent_payment import PaymentGroupAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset
)

class SupportMasterAgent(Agent):
    def __init__(self, mcp_tools:MCPToolset, **kwargs):
        super().__init__(
            name="support_master_agent",
            model=GEMINI_2_5_MODEL,
            instruction=UBER_AGENT_PROMPT,
            # sub_agents are passed to the super class
            # The following line assumes you have a SupportMasterAgent class
            sub_agents=[BillingGroupAgent(), PaymentGroupAgent()],
            tools=[AgentTool(SupportQnAAgent(mcp_tools=mcp_tools))],
            **kwargs
        )