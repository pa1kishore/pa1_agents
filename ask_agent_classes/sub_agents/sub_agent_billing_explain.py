import os
import pathlib
import json
from ask_agent_classes.prompts.billing_prompts import SUPPORT_BILLING_EXPLAIN_AGENT_PROMPT
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from ask_agent_classes.constants import GEMINI_2_5_MODEL
from typing import ClassVar
from ask_agent_classes.sub_agents.sub_agent_qna import SupportQnAAgent

class BillingExplainAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="billing_explain_agent",
            model=GEMINI_2_5_MODEL,
            instruction=SUPPORT_BILLING_EXPLAIN_AGENT_PROMPT,
            # tools=[AgentTool(SupportQnAAgent())],
            **kwargs
        )