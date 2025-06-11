# agents/fit_evaluator.py
from langchain_core.prompts import PromptTemplate

from llm.gpt import get_gpt
from utils.memory import append_to_history

llm = get_gpt()

def run_fit_eval(state):
    prompt = PromptTemplate.from_file("prompts/fit.txt", input_variables=["input", "history"])
    formatted = prompt.format(input=state["input"], history=state["history"])
    response = llm.invoke(formatted)

    state["history"] = append_to_history(state["history"], "직무 적합도 평가자", response.content)

    return state