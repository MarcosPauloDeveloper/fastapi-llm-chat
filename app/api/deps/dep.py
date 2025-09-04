from functools import lru_cache
from app.adapters.openai_client import OpenAIClient
from app.adapters.repositories.thread_store import InMemoryContextStore
from app.use_case.chat_use_case import ChatUseCase


@lru_cache
def get_llm():
    return OpenAIClient()


@lru_cache
def get_store():
    return InMemoryContextStore()


def get_chat_uc() -> ChatUseCase:
    return ChatUseCase(llm=get_llm(), store=get_store())
