from agents.user_proxy import user_proxy
from agents.planner_agent import planner
from agents.shell_agent import shell_agent

if __name__ == "__main__":
    user_proxy.initiate_chat(
        recipient=planner,
        message="현재 폴더 내의 파이썬 파일을 확인해줘."
    )
