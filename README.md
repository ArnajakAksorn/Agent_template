# Agent Template

This project provides a framework to **run agents with an API** using [LangServe](https://docs.langchain.dev/langserve/).  
It is designed to support **multi-agent** systems with a clean modular structure.

---

## 🚀 How to Run

Install dependencies first (if not yet):

```bash
pdm install
```

Run the server:

```bash
pdm run langchain serve --port=8100
```

The API will be available at:

```
http://localhost:8100
```

---

## 🛠 Project Structure

```
.
├── app/
│   ├── main.py             # FastAPI app entrypoint
│
├── modules/
│   ├── main_agent.py        # Combine and orchestrate all agents
│   ├── tools.py             # Shared tools and utilities
│   ├── agent1/
│   │   ├── __init__.py
│   │   ├── node.py          # Nodes (LangGraph nodes if using LangGraph)
│   │   ├── prompt.py        # Prompts for agent1
│   │   └── agent1.py        # Main agent1 code (define `agent1.invoke`)
│   ├── agent2/
│   │   ├── __init__.py
│   │   └── ...              # Other agents (similar structure)
│
├── pyproject.toml           # PDM project configuration
└── README.md
```

---

## ✨ Concept Design

- **Main Agent (`main_agent.py`)**
  - Coordinates multiple agents if needed.
  
- **Tools (`tools.py`)**
  - Common reusable functions for agents.
  
- **Agents (`agent1`, `agent2`, etc.)**
  - **`agent1.py`**: Main logic for the agent (`agent1.invoke` method).
  - **`prompt.py`**: All prompts related to the agent are stored here.
  - **`node.py`**: LangGraph nodes (if the agent uses LangGraph workflow).

---

## 📦 Tech Stack

- [LangChain](https://www.langchain.dev/)
- [LangServe](https://docs.langchain.dev/langserve/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PDM](https://pdm.fming.dev/latest/)
