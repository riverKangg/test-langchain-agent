# brainstorm_assistant/graph/workflow.py
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from agents.expander import expand_idea
from agents.critic import criticize_idea
from agents.selector import select_opinions
from agents.summarizer import summarize_all

from typing import TypedDict

class MyState(TypedDict):
    input: str
    expanded: str
    critique: str
    selected: str
    summary: str

def build_graph():
    graph = StateGraph(MyState)
    graph.add_node("Expand", RunnableLambda(expand_idea))
    graph.add_node("Critic", RunnableLambda(criticize_idea))
    graph.add_node("Selector", RunnableLambda(select_opinions))
    graph.add_node("Summarizer", RunnableLambda(summarize_all))

    graph.set_entry_point("Expand")
    graph.add_edge("Expand", "Critic")
    graph.add_edge("Critic", "Selector")
    graph.add_edge("Selector", "Summarizer")
    graph.add_edge("Summarizer", END)

    return graph.compile()

