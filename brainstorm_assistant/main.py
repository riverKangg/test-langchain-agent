# brainstorm_assistant/main.py
from graph.workflow import build_graph

if __name__ == "__main__":
    chain = build_graph()
    user_input = input("💬 아이디어를 입력하세요: ")
    if user_input == "":
        user_input = \
            """
            아래 조건에 맞는 1인 창업 아이템을 찾아주세요.  
            [조건]  
            - 생성형AI, 에이전트, 멀티 에이전트, MCP 중 하나 이상 활용  
            - 비용 100만원 이하
            - 법률적인 문제가 없는 가벼운 아이디어
            - 직장인이 평일 저녁 및 주말만 활용해서 유지 가능한 서비스
            """

    print("\n⏳ 아이디어 분석 중...\n")
    result = chain.invoke({"input": user_input})

    expanded = result.get("expanded", "(결과 없음)")
    critique = result.get("critique", "(결과 없음)")
    mediated = result.get("mediated", "(결과 없음)")
    summary = result.get("summary", "(결과 없음)")


    # 결과 구성
    markdown_output = f"""# 🧠 브레인스토밍 리포트

## 📌 사용자 입력
{user_input}

## 💡 아이디어 확장
{expanded}

## ⚠️ 비판적 분석
{critique}

## 🧘‍♂️ 선택된 의견
{mediated}

## 🧠 최종 요약 및 실행 제안
{summary}
"""

    # 파일 저장
    with open("brainstorm_result.md", "w", encoding="utf-8") as f:
        f.write(markdown_output)

    print("\n✅ 결과가 'brainstorm_result.md'로 저장되었습니다.")