import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        #"model": "openai/gpt-4o",  # Optional
        "model": "qwen/qwen-2.5-vl-7b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": "Can you code in latex? If you can make some basic latex code."
            }
        ]
    })
)

#url = "https://openrouter.ai/api/v1/models"
#response = requests.get(url)
response = response.json()

print(response["choices"][0]["message"]["content"])