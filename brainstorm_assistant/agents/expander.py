# brainstorm_assistant/agents/expander.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from llm.gpt import get_gpt

# llm = ChatOpenAI()
llm = get_gpt()

def expand_idea(state):
    prompt = PromptTemplate.from_file("prompts/expander.txt", input_variables=["input"])
    formatted = prompt.format(input=state["input"])
    response = llm.invoke(formatted)
    return {**state, "expanded": response.content}

