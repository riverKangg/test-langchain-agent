# brainstorm_assistant/agents/mediator.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from llm.gpt import get_gpt

# llm = ChatOpenAI()
llm = get_gpt()

def mediate_opinions(state):
    prompt = PromptTemplate.from_file("prompts/mediator.txt", input_variables=["expanded", "critique"])
    formatted = prompt.format(expanded=state["expanded"], critique=state["critique"])
    response = llm.invoke(formatted)
    return {**state, "mediated": response.content}