import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, USER_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def generate_answer(question: str, context: str) -> str:
    prompt = USER_PROMPT.format(
        context=context,
        question=question
    )

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content