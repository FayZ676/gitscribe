from typing import List, Optional

from openai import OpenAI
from openai.types.responses import ResponseOutputMessage, ResponseOutputText


class OpenAILLM:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str):
        response = self.client.responses.create(model="gpt-5", input=prompt)
        message_content = _find_message_content(response.output)

        if not message_content or not message_content.content:
            return None

        text = message_content.content[0]
        assert isinstance(text, ResponseOutputText)
        return text.text


def _find_message_content(output: List) -> Optional[ResponseOutputMessage]:
    """Find the first ResponseOutputMessage in the output array."""
    return next(
        (item for item in output if isinstance(item, ResponseOutputMessage)), None
    )
