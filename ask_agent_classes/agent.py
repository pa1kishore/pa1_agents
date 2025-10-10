import os
import pathlib
import json
from .prompts.prompts import UBER_AGENT_PROMPT
from google.adk.agents import Agent
from ask_agent_classes.constants import GEMINI_2_5_MODEL
from .support_master_agent import SupportMasterAgent
from typing import ClassVar
class UberAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="ask_agent_classes",
            model=GEMINI_2_5_MODEL,
            instruction=UBER_AGENT_PROMPT,
            # sub_agents are passed to the super class
            # The following line assumes you have a SupportMasterAgent class
            sub_agents=[SupportMasterAgent()],
            **kwargs
        )

root_agent = UberAgent()