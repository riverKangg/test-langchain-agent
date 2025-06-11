# 🧠 Brainstorm Assistant

LangGraph + LangChain 기반으로 설계된 멀티에이전트 브레인스토밍 도우미입니다.  
사용자의 아이디어를 입력하면, 다양한 관점에서 아이디어를 확장·비판·선택한 뒤 실행 가능한 요약을 생성합니다.

---

## 🚀 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 실행
python main.py
````

결과는 콘솔에 실시간 출력되며, `brainstorm_result.md` 파일로 저장됩니다.

---

## ⚙️ 작동 흐름

```
[사용자 입력]
   ↓
[💡 아이디어 확장 (Expand)]
   ↓
[⚠️ 비판적 분석 (Critic)]
   ↓
[🧘‍♂️ 선택된 의견 (Selector)]
   ↓
[🧠 요약 및 실행 제안 (Summarizer)]
   ↓
[결과 출력 및 저장]
```

각 단계는 LangGraph의 상태 전이(StateGraph)로 정의되어 순차적으로 실행됩니다.

---

## 📁 디렉토리 구조

```
brainstorm_assistant/
├── main.py                  # 실행 진입점
├── agents/                  # 각 에이전트 정의
│   ├── expander.py          # 아이디어 확장
│   ├── critic.py            # 비판
│   ├── selector.py          # 조율
│   └── summarizer.py        # 요약
├── graph/
│   └── workflow.py          # LangGraph 상태머신 정의
├── prompts/                 # 프롬프트 템플릿
│   ├── expander.txt
│   ├── critic.txt
│   ├── selector.txt
│   └── summarizer.txt
├── brainstorm_result.md     # 결과 저장 파일 (실행 시 생성)
└── requirements.txt         # 의존성 명세
```

---

## 🧩 사용 기술 및 이유

| 기술 스택          | 설명                                |
| -------------- | --------------------------------- |
| **LangChain**  | LLM 기반 처리, 프롬프트 템플릿 관리            |
| **LangGraph**  | 멀티에이전트 흐름을 상태 기반으로 관리하는 FSM 프레임워크 |
| **OpenAI GPT** | 아이디어 확장/비판/요약 생성에 사용되는 LLM        |
| **Python**     | 전체 로직 구성 (3.8 이상 권장)              |

### 🔍 왜 LangGraph인가?

* 단계별 흐름을 **명시적이고 유연하게 구성**
* 추후 **사용자 피드백 기반 루프** 등 복잡한 논리 추가 가능
* 유지보수가 쉬운 **노드 기반 분리 구조**

---

## 📌 예시 입력 & 출력

**입력 예시:**

```
멀티에이전트를 활용한 1인 창업아이템 구상해줘.
```

**출력 예시:**

```markdown
## 💡 아이디어 확장
- 콘텐츠 기획 자동화 시스템
- 브레인스토밍 조력 도우미 SaaS
...

## ⚠️ 비판적 분석
- 기술 구현 진입장벽 존재
- 시장 진입 시 유사 서비스와 차별화 어려움
...

## 🧘‍♂️ 조율된 의견
- MVP 수준으로 시작하여 반응 기반 피벗을 권장
...

## 🧠 최종 요약 및 실행 제안
멀티에이전트 기반 창업은 초기 진입장벽이 있으나, 적은 기능부터 테스트 가능한 방향을 설정하는 것이 현실적...
```

---

## 📮 기여 / 확장 제안

* [ ] Web UI (Gradio/Streamlit 등) 추가
* [ ] 사용자 피드백 받아 루프 재귀 흐름 구성
* [ ] 다양한 에이전트 역할 추가 (시장조사, 리스크 평가 등)

---