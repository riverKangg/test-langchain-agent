from autogen import AssistantAgent
from tools.shell_tool import shell_tool  # LangChain tool

def run_shell_command(command: str) -> str:
    return shell_tool.run(command)

shell_agent = AssistantAgent(
    name="shell_agent",
    llm_config=False,  # LLM 없이, 직접 실행만
    system_message="너는 명령어를 실제로 실행하는 실행자야. 명령어를 받아서 실행 결과만 리턴해.",
    # code_execution_config={"executor": run_shell_command}
)