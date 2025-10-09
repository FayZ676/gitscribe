import os

from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4.1", input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
