# ai_interview_simulator/main.py
from graph.interview_graph import build_graph

def format_history(history):
    lines = []
    for entry in history:
        role = entry["role"]
        message = entry["message"]
        lines.append(f"### {role}\n{message}\n")
    return "\n".join(lines)

if __name__ == "__main__":
    chain = build_graph()

    user_input = input("👤 지원자 자기소개를 입력하세요: ")
    if user_input == "":
        user_input = """안녕하세요. 저는 5년간 웹 백엔드 개발자로 일해온 이현호입니다. Java와 Spring Boot 기반의 시스템을 주로 개발했고, 최근 2년은 AWS 환경에서 마이크로서비스 아키텍처 전환 프로젝트를 리딩했습니다. 서비스 안정성과 확장성을 고려한 설계에 관심이 많으며, DevOps 문화에도 익숙합니다. 팀원들과의 협업과 코드 리뷰를 중요하게 생각하며, 사용자 중심의 문제 해결을 추구합니다. 앞으로는 대규모 트래픽을 처리하는 플랫폼 백엔드 개발에 기여하고 싶습니다."""
    state = {"input": user_input, "history": []}

    print("\n⏳ 면접 질문 생성 중...\n")
    result = chain.invoke(state)

    # Markdown 형식 출력 정리
    history_markdown = format_history(state["history"])
    markdown_output = f"""# 📄 AI 면접 리포트

## 👤 지원자 입력
{user_input}

---

## 🧠 면접 질문
{history_markdown}


"""

    # 파일로 저장
    with open("interview_question.md", "w", encoding="utf-8") as f:
        f.write(markdown_output)

    print("\n✅ 면접 질문이 'interview_question.md' 파일로 저장되었습니다.")
