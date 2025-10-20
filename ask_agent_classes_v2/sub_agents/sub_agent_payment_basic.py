import os
import pathlib
import json
from ask_agent_classes_v2.prompts.payment_prompts import SUPPORT_PAYMENT_BASIC_AGENT_PROMPT
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from ask_agent_classes_v2.constants import GEMINI_2_5_MODEL
from typing import ClassVar

class PaymentBasicAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="payment_basic_agent",
            model=GEMINI_2_5_MODEL,
            instruction=SUPPORT_PAYMENT_BASIC_AGENT_PROMPT,
            # tools=[AgentTool(SupportQnAAgent())],
            **kwargs
        )