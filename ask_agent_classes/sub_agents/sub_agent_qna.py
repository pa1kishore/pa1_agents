import os
import pathlib
import json
from ask_agent_classes.prompts.prompts import SUPPORT_QNA_AGENT_PROMPT
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset
)
# from google.adk.tools import AgentTool
from ask_agent_classes.constants import DEFAULT_MODEL
from typing import ClassVar
class SupportQnAAgent(Agent):
    def __init__(self,mcp_tools:MCPToolset, **kwargs):
        super().__init__(
            name="support_qna_agent",
            model=DEFAULT_MODEL,
            instruction=SUPPORT_QNA_AGENT_PROMPT,
            tools=[mcp_tools],
            **kwargs
        )