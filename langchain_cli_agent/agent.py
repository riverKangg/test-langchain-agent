# agent.py
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from tools.shell_tool import shell_tool

llm = ChatOpenAI(temperature=0)

tools = [shell_tool]  # 여기에 필요한 tool 추가

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

def run_agent(prompt: str):
    return agent.run(prompt)
