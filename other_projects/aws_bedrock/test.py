"""Test AWS BedRock API"""

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
# -----------------------------------------------------------
# 1️⃣  Configure these values
# -----------------------------------------------------------

# Paste your API key here OR set it as an environment variable
# export BEDROCK_API_KEY="your_api_key_here"
API_KEY = os.getenv(
    "BEDROCK_API_KEY",
    os.getenv("BEDROCK_API_KEY"),
)

# Choose your AWS region where the model is deployed
REGION = "us-east-1"

# Use a cheap model for testing
MODEL_ID = "amazon.titan-text-lite-v1"  # or anthropic.claude-3-haiku-20240307

# -----------------------------------------------------------
# 2️⃣  Prepare request payload
# -----------------------------------------------------------

endpoint = f"https://bedrock-runtime.{REGION}.amazonaws.com/model/{MODEL_ID}/invoke"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

payload = {
    "inputText": "Write a one-line joke about AWS cloud engineers.",
    "textGenerationConfig": {"maxTokenCount": 50, "temperature": 0.7, "topP": 0.9},
}

# -----------------------------------------------------------
# 3️⃣  Call Bedrock endpoint
# -----------------------------------------------------------

try:
    print(f"Invoking {MODEL_ID} in {REGION} ...")
    response = requests.post(endpoint, headers=headers, json=payload, verify=False)
    response.raise_for_status()

    result = response.json()
    print("\nSuccess!")
    print(json.dumps(result, indent=2))

except requests.exceptions.HTTPError as e:
    print("\nAPI call failed")
    print("Status:", e.response.status_code)
    print("Body:", e.response.text)
except Exception as e:
    print("\nUnexpected error:", e)
