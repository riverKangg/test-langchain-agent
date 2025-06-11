# AI 면접관 시뮬레이터

### ✅ 디렉토리 구조

```
ai_interview_simulator/
├── agents/
│   ├── tech_interviewer.py         # 기술 면접관 에이전트
│   ├── hr_interviewer.py           # HR 면접관 에이전트
│   └── fit_evaluator.py            # 직무 적합도 평가 에이전트
├── graph/
│   └── interview_graph.py          # LangGraph 정의 및 흐름 설정
├── prompts/
│   ├── tech_prompt.txt             # 기술 면접 질문 프롬프트
│   ├── hr_prompt.txt               # HR 질문 프롬프트
│   └── fit_prompt.txt              # 직무 적합도 평가 프롬프트
├── utils/
│   └── memory.py                   # 공유 memory 및 context 저장 유틸
├── main.py                         # 실행 진입점
└── requirements.txt                # 필요한 패키지 명세
```
