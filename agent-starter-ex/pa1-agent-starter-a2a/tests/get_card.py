import google.auth
import requests

# ----------------------------------------
# CONFIGURATION — fill these in
# ----------------------------------------
PROJECT_ID = "lexical-helix-462005-m6"
LOCATION = "us-central1"  # or where your agent is deployed
AGENT_ID = "4489363150814052352"  # looks like: 1234567890123

# This is your AGENT ENGINE "public endpoint"
ENGINE_BASE = (
    f"https://{LOCATION}-aiplatform.googleapis.com/v1/"
    f"projects/{PROJECT_ID}/locations/{LOCATION}/agents/{AGENT_ID}"
)

# The special endpoint for AUTHENTICATED agent card
GET_CARD_URL = f"{ENGINE_BASE}:handleAuthenticatedAgentCard"

# ----------------------------------------
# AUTHENTICATE using GCloud credentials
# ----------------------------------------
creds, _ = google.auth.default(scopes=[
    "https://www.googleapis.com/auth/cloud-platform"
])
creds.refresh(requests.Request())
token = creds.token

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# ----------------------------------------
# CALL THE API
# ----------------------------------------
print("Calling:", GET_CARD_URL)
response = requests.post(GET_CARD_URL, headers=headers, json={})

if response.status_code != 200:
    print("Error:", response.status_code, response.text)
    exit()

card = response.json()
print("\n=== A2A AGENT CARD ===")
print(card)

# Extract base URL if present
try:
    base_url = card["agentCard"]["url"]
    print("\nA2A BASE URL =", base_url)
except:
    print("\nNo 'url' found in agent card. A2A may not be enabled.")
