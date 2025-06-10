# main.py
from agent import run_agent

if __name__ == "__main__":
    print("💬 자연어 명령어를 입력하세요 (종료: exit)")
    while True:
        query = input(">>> ")
        if query.lower() in ("exit", "quit"):
            break
        response = run_agent(query)
        print(response)
