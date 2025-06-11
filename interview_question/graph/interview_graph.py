from langgraph.graph import StateGraph
from agents.tech_interviewer import run_tech_interview
from agents.hr_interviewer import run_hr_interview
from agents.fit_evaluator import run_fit_eval

from typing import TypedDict

class MyState(TypedDict):
    input: str
    history: list

def build_graph():
    graph = StateGraph(MyState)
    graph.add_node("tech", run_tech_interview)
    graph.add_node("hr", run_hr_interview)
    graph.add_node("fit", run_fit_eval)

    graph.set_entry_point("tech")
    graph.add_edge("tech", "hr")
    graph.add_edge("hr", "fit")

    return graph.compile()