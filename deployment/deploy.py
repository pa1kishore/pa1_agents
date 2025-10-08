# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
from datetime import datetime
# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp
from ask_agent.agent import root_agent
import logging
import os
from dotenv import set_key, load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
STAGING_BUCKET = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
AGENT_DISPLAY_NAME = 'ask_agent'
AGENT_ID='sdsdgsdfg'

ENV_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))

vertexai.init(
    project=GOOGLE_CLOUD_PROJECT,
    location=GOOGLE_CLOUD_LOCATION,
    staging_bucket=STAGING_BUCKET,
)

# Function to update the .env file
def update_env_file(agent_engine_id, env_file_path):
    """Updates the .env file with the agent engine ID."""
    try:
        set_key(env_file_path, "AGENT_ENGINE_ID", agent_engine_id)
        logger.info(f"Updated AGENT_ENGINE_ID in {env_file_path} to {agent_engine_id}")
    except Exception as e:
        logger.info(f"Error updating .env file: {e}")

logger.info("deploying app...")

app = AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

logging.debug("deploying agent to agent engine:")

def upsert_agent():
    new_agent=None
    try:
        # Try to get the existing agent
        logging.info(f"Checking for existing agent with display name: {AGENT_DISPLAY_NAME}...")
        existing_agents = agent_engines.list()
        if existing_agents !=None:
            for i in iter(existing_agents):
                logging.info(f'agents :{i.name}')
        new_agent = agent_engines.get(AGENT_ID)
        
        # If it exists, update it
        logging.info("Agent found. Updating the existing agent...")
        updated_app = new_agent.update(
            agent_engine=app,
            display_name= AGENT_DISPLAY_NAME,
            description= f'{AGENT_DISPLAY_NAME} updated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            # Update other configurable parameters if needed
        )
        logging.info(f"Successfully updated agent: {updated_app.display_name}")

    except Exception as e:
        # If the agent doesn't exist, create it
        logging.error(f'Agent not found. {e}')
        logging.info("Agent not found. Creating a new agent...")
        new_agent = agent_engines.create(
                        app,
                        display_name=AGENT_DISPLAY_NAME,
                        description= f'{AGENT_DISPLAY_NAME} created on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                        requirements=[
                            "google-cloud-aiplatform[adk,agent-engines]>=1.100.0,<2.0.0",
                            "google-adk>=1.5.0,<2.0.0",
                            "python-dotenv",
                            "google-cloud-secret-manager"
                        ],
                        extra_packages=[
                            "./ask_agent",
                        ],
                    )
        logging.info(f"Successfully created new agent: {new_agent.display_name}")

    return new_agent

remote_app = upsert_agent()
# log remote_app
logging.info(f"Deployed agent to Vertex AI Agent Engine successfully, resource name: {remote_app.resource_name}")

# Update the .env file with the new Agent Engine ID
update_env_file(remote_app.resource_name, ENV_FILE_PATH)