#!/usr/bin/env python

import os
import requests

# Get API key
api_key = os.environ.get("API_KEY")
if not api_key:
    print("Error: API_KEY not found in environment variables.")
    exit(1)

# Define API endpoint and headers
endpoint = "https://api.openai.com/v1/completions"
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

while True:
    try:
        # Get user input
        prompt = input("What is your question? (or 'exit' to quit) ")
        if prompt.lower() == "exit":
            break

        # Define payload
        payload = {
            "prompt": prompt,
            "model": "text-davinci-003",
            "max_tokens": 2048,
            "temperature": 0.5,
        }

        # Send post request
        response = requests.post(endpoint, json=payload, headers=headers)

        # Simple error
        if response.status_code != 200:
            print("An error occurred while generating a response from the model.")
            print(response.text)
            break

        # Print response
        answer = response.json()["choices"][0]["text"]
        print(answer)
    except KeyboardInterrupt:
        break

print("\nExiting...")