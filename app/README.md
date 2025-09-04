# FastAPI OpenAI Chat API

A lightweight conversational API built with **FastAPI** and the **OpenAI Responses API**.  
It maintains per-session context in-memory (using `resp_id`) and appends assistant replies to the conversation flow.

This project was designed as a clean, production-ready prototype for demonstrating **LLM-powered APIs**, suitable for deployment on **AWS (App Runner, EC2, or Lambda)** or any container platform.


## Features

- 🔹 **FastAPI** backend with modular architecture (adapters, use cases, repositories).
- 🔹 **OpenAI Responses API** integration.
- 🔹 **In-memory context store** for managing conversations via `resp_id`.
- 🔹 **CORS enabled** for browser-based clients.
- 🔹 **Dockerized** for easy deployment.
- 🔹 Example deployment instructions for **AWS App Runner** and **EC2**.


## Project Structure

```

app/
api/
routers/        # FastAPI routers
deps/           # dependency injection (OpenAI client + store)
adapters/
openai\_client.py
repositories/
thread\_store.py
core/
config.py       # settings via pydantic-settings
schemas/          # request/response models
use\_case/         # business logic
main.py           # FastAPI app factory

````

## Requirements

- Python **3.11+**
- Dependencies listed in `requirements.txt`:
  - fastapi
  - uvicorn[standard]
  - openai
  - pydantic-settings


## Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/MarcosPauloDeveloper/fastapi-llm-chat.git
   cd <repo>
```

2. **Create .env file**

   ```env
   OPENAI_API_KEY=sk-...
   MODEL=gpt-5-nano
   ```

3. **Install dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Start the API**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Test it**

   ```bash
   curl -s -X POST http://localhost:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"resp_id":"demo","message":"What is the capital of France?"}'
   ```

## Docker

### Build the image

```bash
docker build -t fastapi-openai-chat:latest .
```

### Run the container

```bash
docker run -d --name fastapi-openai-chat \
  -p 8000:8000 \
  -e OPENAI_API_KEY=sk-... \
  -e MODEL=gpt-5-nano \
  fastapi-openai-chat:latest
```

## Endpoints

### `POST /chat`

Send a message to the assistant.

**Request body**

```json
{
  "resp_id": "user-123",
  "message": "Hello, who are you?"
}
```

* `resp_id`: conversation/session identifier. If empty, the API returns the new OpenAI response ID.
* `message`: user input.

**Response**

```json
{
  "reply": "Hi! I am your helpful assistant.",
  "id": "resp_abc123"
}
```

### `GET /chat/{resp_id}/history` (optional, if exposed)

Returns accumulated conversation for the given `resp_id`.

### `DELETE /chat/{resp_id}` (optional, if exposed)

Clears the conversation context for the given `resp_id`.


## Deployment

### AWS App Runner (recommended)

1. Push your code and Dockerfile to GitHub.
2. In AWS App Runner:

   * Source: **GitHub repository**
   * Build: use your **Dockerfile**
   * Environment variables: set `OPENAI_API_KEY`, `MODEL`
   * Port: `8000`
3. After deployment, test via:

   ```bash
   curl -s -X POST https://<your-app-url>/chat \
     -H "Content-Type: application/json" \
     -d '{"resp_id":"demo","message":"Hello!"}'
   ```

### AWS EC2 (Docker)

```bash
ssh -i your-key.pem ubuntu@<EC2-IP>
sudo apt update && sudo apt -y install docker.io
git clone https://github.com/MarcosPauloDeveloper/fastapi-llm-chat.git
cd <repo>
docker build -t fastapi-openai-chat .
docker run -d -p 80:8000 \
  -e OPENAI_API_KEY=sk-... \
  -e MODEL=gpt-5-nano \
  fastapi-openai-chat
```

Your API will be available at `http://<EC2-IP>/chat`.


## License

MIT License. Free to use and adapt.
