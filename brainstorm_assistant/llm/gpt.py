import os
from langchain_openai import ChatOpenAI

def get_gpt():
    return ChatOpenAI(
        model="gpt-4o",
        api_key=os.environ.get("OPENAI_API_KEY")
    )