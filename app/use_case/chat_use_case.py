from app.adapters.openai_client import OpenAIClient
from app.adapters.repositories.thread_store import InMemoryContextStore


class ChatUseCase:
    def __init__(self, llm: OpenAIClient, store: InMemoryContextStore):
        self.llm = llm
        self.store = store

    def handle_message(self, resp_id: str, user_message: str):
        try:
            ctx = self.store.get_context(resp_id)
            ctx.append({"role": "user", "content": user_message})
            reply, new_ctx, new_resp_id = self.llm.respond(ctx)
            self.store.set_context(resp_id, new_ctx)
            return reply, resp_id if resp_id else new_resp_id
        except RuntimeError as e:
            return f"⚠️ Error while processing: {str(e)}", resp_id
        except Exception as e:
            return f"⚠️ Unexpected error: {str(e)}", resp_id

    def history(self, resp_id: str):
        return self.store.get_context(resp_id)

    def clear(self, resp_id: str):
        self.store.clear(resp_id)
