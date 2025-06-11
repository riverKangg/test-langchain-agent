# agents/hr_interviewer.py
from langchain_core.prompts import PromptTemplate

from llm.gpt import get_gpt
from utils.memory import append_to_history

def run_hr_interview(state):
    prompt = PromptTemplate.from_file("prompts/hr.txt", input_variables=["input", "history"])
    formatted = prompt.format(input=state["input"], history=state["history"])

    llm = get_gpt()
    response = llm.invoke(formatted)

    state["history"] = append_to_history(state["history"], "HR 면접관", response.content)
    
    return state