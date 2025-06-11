# brainstorm_assistant/agents/critic.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from llm.gpt import get_gpt

# llm = ChatOpenAI()
llm = get_gpt()

def criticize_idea(state):
    prompt = PromptTemplate.from_file("prompts/critic.txt", input_variables=["expanded"])
    formatted = prompt.format(expanded=state["expanded"])
    response = llm.invoke(formatted)
    return {**state, "critique": response.content}