import asyncio
import vertexai
from google.genai import types

PROJECT_ID = "lexical-helix-462005-m6"
LOCATION = "us-central1"  # or where your agent is deployed
RESOURCE_ID = "4489363150814052352"  # looks like: 1234567890123
RESOURCE_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{RESOURCE_ID}"

async def main():
    client = vertexai.Client(
        project=PROJECT_ID,
        location=LOCATION,
        http_options=types.HttpOptions(api_version="v1beta1")
    )

    remote_agent = client.agent_engines.get(name=RESOURCE_NAME)

    print(remote_agent)

    response = await remote_agent.handle_authenticated_agent_card()
    print("\n=== A2A AGENT CARD ===")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())