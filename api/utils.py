import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def get_gpt_response(message):
    if message[0]["role"] != "system":
        message.insert(0, {"role": "system", "content": "You are a helpful assistant designed to output JSON."})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=message,
        temperature=0,
        max_tokens=512
    )

    return response.choices[0].message.content



message = [
    {"role": "user", "content": "Чат ГПТ очень умный"},
    {"role": "assistant", "content": "Благодарюю. Чем могу быть полезен?"},
    {"role": "user", "content": "А что ты умеешь?"}
  ]

print(get_gpt_response(message))
