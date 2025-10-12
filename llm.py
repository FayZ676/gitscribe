from openai import OpenAI


class OpenAILLM:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str):
        response = self.client.responses.create(
            model="gpt-4.1",
            input=prompt,
        )
        return response.output[0].content[0].text
