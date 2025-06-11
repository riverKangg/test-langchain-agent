# brainstorm_assistant/agents/selector.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from llm.gpt import get_gpt

# llm = ChatOpenAI()
llm = get_gpt()

def select_opinions(state):
    prompt = PromptTemplate.from_file("prompts/selector.txt", input_variables=["expanded", "critique"])
    formatted = prompt.format(expanded=state["expanded"], critique=state["critique"])
    response = llm.invoke(formatted)
    return {**state, "selected": response.content}