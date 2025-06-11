# brainstorm_assistant/agents/summarizer.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from llm.gpt import get_gpt

# llm = ChatOpenAI()
llm = get_gpt()

def summarize_all(state):
    prompt = PromptTemplate.from_file("prompts/summarizer.txt", input_variables=["expanded", "critique", "mediated"])
    response = llm.invoke(prompt.format(**state))
    return {**state, "summary": response.content}