import os
import pathlib
import json
from ask_agent_classes.prompts.prompts import SUPPORT_QNA_AGENT_PROMPT
from google.adk.agents import Agent
# from google.adk.tools import AgentTool
from ask_agent_classes.constants import GEMINI_2_5_MODEL
from typing import ClassVar
class SupportQnAAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="support_qna_agent",
            model=GEMINI_2_5_MODEL,
            instruction=SUPPORT_QNA_AGENT_PROMPT,
            **kwargs
        )