
from autogen import AssistantAgent
from agents.shell_agent import shell_agent

planner = AssistantAgent(
    name="planner_agent",
    llm_config={"config_list": [{"model": "gpt-4"}]},  # 또는 gpt-3.5
    system_message=(
        "당신은 주어진 작업을 bash 명령어로 분해해서 실행 계획을 수립해야 합니다. "
        "실행은 shell_agent에게 맡기세요. 명령어를 직접 실행하지 마세요."
    )
)

planner.register_function(
    # name="delegate_to_shell_agent",
    function_map={
        "delegate_to_shell_agent": lambda command: shell_agent.receive(command)
    },
    # description="shell_agent에게 명령을 넘긴다"
)

# https://docs.ag2.ai/latest/docs/api-reference/autogen/AssistantAgent/#autogen.AssistantAgent.system_message