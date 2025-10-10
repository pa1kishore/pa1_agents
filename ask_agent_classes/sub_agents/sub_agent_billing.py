import os
import pathlib
import json
from ask_agent_classes.prompts.billing_prompts import SUPPORT_BILLING_GROUP_AGENT_PROMPT
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from ask_agent_classes.constants import GEMINI_2_5_MODEL
from ask_agent_classes.sub_agents.sub_agent_billing_basic import BillingBasicAgent
from ask_agent_classes.sub_agents.sub_agent_billing_compare import BillingCompareAgent
from ask_agent_classes.sub_agents.sub_agent_billing_explain import BillingExplainAgent

class BillingGroupAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="billing_group_agent",
            model=GEMINI_2_5_MODEL,
            instruction=SUPPORT_BILLING_GROUP_AGENT_PROMPT,
            tools=[AgentTool(BillingBasicAgent()), AgentTool(BillingCompareAgent()), AgentTool(BillingExplainAgent())],
            **kwargs
        )