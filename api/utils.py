import os

from openai import OpenAI
from gigachat import GigaChat
import fastjsonschema
from dotenv import load_dotenv

load_dotenv()

giga_schema = {"type": "string"}

gpt_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "role": {
                "type": "string",
                "enum": ["system", "user", "assistant"]
            },
            "content": {
                "type": "string"
            }
        },
        "required": ["role", "content"],
        "additionalProperties": False
    },
    "minItems": 1
}


def get_gpt_response(message):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0,
        max_tokens=512
    )

    return response.choices[0].message.content


def get_giga_response(message):
    with GigaChat(credentials=os.getenv('GIGACHAT_API_KEY'), verify_ssl_certs=False) as giga:
        response = giga.chat(message)
        return response.choices[0].message.content


def validate_message(message, schema):
    if schema == 'gpt':
        validator = fastjsonschema.compile(gpt_schema)
        validator(message)
    elif schema == 'giga':
        validator = fastjsonschema.compile(giga_schema)
        validator(message)
