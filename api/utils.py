import os

from openai import OpenAI
from gigachat import GigaChat
import fastjsonschema
from dotenv import load_dotenv

load_dotenv()


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
        return (response.choices[0].message.content)



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
    "minItems": 2
}

def validate_gpt(message):
    validator = fastjsonschema.compile(gpt_schema)
    validator(message)
    try:
        validator(message)
    except fastjsonschema.JsonSchemaException as e:
        return (f"Data failed validation: {e}")



messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]



validate_gpt(messages)
