# 멀티에이전트를 활용한 1인 창업아이템 구상해줘.

# brainstorm_assistant/main.py
from graph.workflow import build_graph

if __name__ == "__main__":
    chain = build_graph()
    user_input = input("💬 아이디어를 입력하세요: ")
    result = chain.invoke({"input": user_input})
    print("\n🧠 브레인스토밍 결과:\n")
    print(result['summary'])


# brainstorm_assistant/agents/__init__.py
# 빈 파일 (패키지 인식용)


# brainstorm_assistant/agents/expander.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI()

def expand_idea(state):
    # prompt = PromptTemplate.from_file("prompts/expander.txt", input_variables=["input"])
    # return {"expanded": llm(prompt.format(input=state["input"]))}

    prompt = PromptTemplate.from_file("prompts/expander.txt", input_variables=["input"])
    formatted = prompt.format(input=state["input"])
    response = llm.invoke(formatted)
    return {"expanded": response.content}


# brainstorm_assistant/agents/critic.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI()

def criticize_idea(state):
    prompt = PromptTemplate.from_file("prompts/critic.txt", input_variables=["expanded"])
    return {"critique": llm(prompt.format(expanded=state["expanded"]))}


# brainstorm_assistant/agents/mediator.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI()

def mediate_opinions(state):
    prompt = PromptTemplate.from_file("prompts/mediator.txt", input_variables=["expanded", "critique"])
    return {"mediated": llm(prompt.format(expanded=state["expanded"], critique=state["critique"]))}


# brainstorm_assistant/agents/summarizer.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI()

def summarize_all(state):
    prompt = PromptTemplate.from_file("prompts/summarizer.txt", input_variables=["expanded", "critique", "mediated"])
    summary = llm(prompt.format(**state))
    return {"summary": summary}


# brainstorm_assistant/graph/__init__.py
# 빈 파일 (패키지 인식용)


# brainstorm_assistant/graph/workflow.py
from langgraph.graph import StateGraph, END
from langchain.schema import RunnableLambda
from agents.expander import expand_idea
from agents.critic import criticize_idea
from agents.mediator import mediate_opinions
from agents.summarizer import summarize_all

def build_graph():
    graph = StateGraph()
    graph.add_node("Expand", RunnableLambda(expand_idea))
    graph.add_node("Critic", RunnableLambda(criticize_idea))
    graph.add_node("Mediator", RunnableLambda(mediate_opinions))
    graph.add_node("Summarizer", RunnableLambda(summarize_all))

    graph.set_entry_point("Expand")
    graph.add_edge("Expand", "Critic")
    graph.add_edge("Critic", "Mediator")
    graph.add_edge("Mediator", "Summarizer")
    graph.add_edge("Summarizer", END)

    return graph.compile()


# brainstorm_assistant/prompts/expander.txt
사용자의 아이디어는 다음과 같습니다:
"""
{input}
"""
이 아이디어를 현실적이고 창의적인 방향으로 3가지 이상 확장해주세요.


# brainstorm_assistant/prompts/critic.txt
다음은 확장된 아이디어입니다:
"""
{expanded}
"""
이 아이디어들에 대해 논리적/현실적인 관점에서 약점이나 주의할 점을 지적해주세요.


# brainstorm_assistant/prompts/mediator.txt
다음은 확장된 아이디어입니다:
"""
{expanded}
"""
그리고 이에 대한 비판입니다:
"""
{critique}
"""
양측을 조율하는 중립적 의견을 생성해주세요. 주요 논점을 요약하고 조정 방향을 제안해주세요.


# brainstorm_assistant/prompts/summarizer.txt
- 확장된 아이디어:
"""
{expanded}
"""
- 비판:
"""
{critique}
"""
- 조율된 의견:
"""
{mediated}
"""

이 흐름을 기반으로 핵심 제안 요약 및 사용자가 참고할 수 있는 실행 가능한 조언을 제공해주세요.


# brainstorm_assistant/requirements.txt
langchain
langgraph
openai
