from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def get_gpt_response(message):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0,
        max_tokens=512
    )

    return response.choices[0].message.content





