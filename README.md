```markdown
# 🛠️ AI Agent Server Template

This project provides a scalable, production-ready framework to **serve AI agents via API** using [FastAPI](https://fastapi.tiangolo.com/), [LangServe](https://docs.langchain.dev/langserve/), and [LangChain](https://www.langchain.dev/).

It is designed to support **multi-agent systems**, clean modularization, and future extensibility (e.g., pluggable chat histories, multiple LLM providers).

---

## 🚀 Quickstart

1. **Install dependencies**

```bash
pdm install
```

2. **Run the server**

```bash
pdm run python -m app.server
```
or 
```bash
pdm run langchain serve
```


> The API will be available at:
> ```
> http://localhost:8000
> ```

---

## 🧩 Project Structure

```
.
├── app/
│   ├── server.py            # FastAPI server entrypoint
│   ├── routes.py            # API routes setup (connect chains to API)
│   ├── utils.py             # Request config modifiers and shared helpers
│   ├── client.ipynb         # Client example notebook (for testing APIs)
│   └── __init__.py
├── chat_histories/          # (Temporary) Local chat history storage (file-based)
│   └── user_id/             # Conversation history files (one JSON per session)
├── core/
│   ├── config.py            # Load environment variables and settings
│   ├── model.py             # Model loader (e.g., AzureChatOpenAI, OpenAI)
│   ├── tools.py             # Shared tools across agents
│   ├── schemas.py           # Input/Output data schemas (TypedDicts, etc.)
│   ├── agent_call.py        # Core agent orchestration logic
│   ├── adapters/
│   │   └── chat_history/
│   │       └── file_history.py  # Local file-based chat history adapter
│   ├── agents/              # Agents implementation
│   │   ├── pirate_agent/
│   │   │   ├── pirate.py    # Pirate agent logic
│   │   │   ├── prompt.py    # Prompts specific to pirate agent
│   │   │   └── __init__.py
│   │   ├── agent2/
│   │   │   └── __init__.py  # Placeholder for another agent
│   │   └── __init__.py
│   └── __init__.py
├── pyproject.toml           # Project and dependency configuration (PDM)
├── pdm.lock                 # Lock file for dependencies
└── README.md                # Project documentation

```
## 🔌 API Endpoints

This server is built using FastAPI and comes with interactive endpoints to help you test and interact with the agents.

### Invoke Endpoint
- **Path:** `/invoke`
- **Method:** `POST`
- **Description:**  
  Invoke an agent’s chain with a given input. The endpoint accepts a JSON payload (for example, a `human_input` along with configuration options like `user_id` and `conversation_id`).
- **Example Payload:**
  ```json
  {
    "human_input": "What is the weather today?",
    "configurable": {
      "user_id": "user123",
      "conversation_id": "conv456"
    }
  }
  ```

### Stream Endpoint
- **Path:** `/stream`
- **Method:** `POST`
- **Description:**  
  Invoke the chain in streaming mode. This endpoint returns partial results as they are generated, which is especially useful for real-time applications.

### Interactive Documentation (Swagger)
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)  
  Use the Swagger UI to interact with and test the API endpoints.

## ℹ️ How to Use

1. **Invoke an Agent:**
   - Send a `POST` request to `/invoke` with the JSON payload as shown above.
   - Receive a JSON response with the agent's output.

2. **Stream Agent Response:**
   - Send a `POST` request to `/stream` with a similar payload and receive a streaming response.

3. **Review the API Docs:**
   - Visit [http://localhost:8000/docs](http://localhost:8000/docs) in your browser to test out the API endpoints interactively.

---

## ✨ Concept Design

| Layer | Responsibility |
|:---|:---|
| `app/` | API serving (FastAPI app, route binding, request schemas, adapters) |
| `core/` | Business logic (chains, prompts, models, agents, tools) |

- `app/` is **lightweight and stateless**.
- `core/` contains **all AI/agent logic**.
- **Adapters** allow flexible backend storage (e.g., chat history can swap from file to database/API easily).
- **Agents** are isolated under `core/agents/` for clean multi-agent support.

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — high-performance API framework
- [LangServe](https://docs.langchain.dev/langserve/) — serve LangChain Runnables via API
- [LangChain](https://www.langchain.dev/) — LLM application framework
- [PDM](https://pdm.fming.dev/latest/) — Python dependency manager
- [Azure OpenAI / OpenAI API](https://learn.microsoft.com/en-us/azure/ai-services/openai/) — LLM provider

---

## 🔮 Future Plans

- **Chat History**:  
  - Currently using **local file storage**.
  - Easy to switch to **API backend** or **database backend** via adapter pattern.
  
- **Multi-Agent Orchestration**:  
  - Support running multiple agents, each with its own chain, prompts, and logic.
  
- **Monitoring and Logging**:  
  - Add tracing and logging to track API usage and agent conversations.

---

## ⚡ How to Add a New Agent

1. Create a new folder inside `core/agents/`, e.g., `agent3/`
2. Define your:
    - `agent.py` — main agent logic
    - `prompt.py` — prompts specific to the agent
    - `node.py` — LangGraph nodes (if needed)
3. Wrap your agent's chain with `wrap_chain_with_history()` from `core/chain/utils.py`
4. Register the agent in `core/setup.py` or make a new route if needed.
