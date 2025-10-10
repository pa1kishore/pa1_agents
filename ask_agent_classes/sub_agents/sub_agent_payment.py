import os
import pathlib
import json
from ask_agent_classes.prompts.billing_prompts import SUPPORT_BILLING_GROUP_AGENT_PROMPT
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from ask_agent_classes.constants import GEMINI_2_5_MODEL
from ask_agent_classes.sub_agents.sub_agent_payment_basic import PaymentBasicAgent
from ask_agent_classes.sub_agents.sub_agent_payment_make_payment import PaymentMakePaymentAgent
from ask_agent_classes.sub_agents.sub_agent_payment_schedule import PaymentScheduleAgent

class PaymentGroupAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="payment_group_agent",
            model=GEMINI_2_5_MODEL,
            instruction=SUPPORT_BILLING_GROUP_AGENT_PROMPT,
            tools=[AgentTool(PaymentBasicAgent()), AgentTool(PaymentMakePaymentAgent()), AgentTool(PaymentScheduleAgent())],
            **kwargs
        )