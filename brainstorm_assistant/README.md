# brainstorm_assistant

### LangGraph 상태 흐름도
```
[Start] 
   ↓ 
[Idea Expander] 
   ↓ 
[Critic] 
   ↓ 
[Mediator] 
   ↓ 
[Summarizer] 
   ↓ 
[End]
```

### 📁 디렉토리 구조
```
brainstorm_assistant/
├── main.py
├── agents/
│   ├── __init__.py
│   ├── expander.py
│   ├── critic.py
│   ├── mediator.py
│   └── summarizer.py
├── graph/
│   ├── __init__.py
│   └── workflow.py
├── prompts/
│   ├── expander.txt
│   ├── critic.txt
│   ├── mediator.txt
│   └── summarizer.txt
└── requirements.txt
```