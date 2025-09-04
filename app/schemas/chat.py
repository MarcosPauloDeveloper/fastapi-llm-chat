from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    resp_id: str = Field("", example="user-123")
    message: str


class ChatResponse(BaseModel):
    reply: str
    id: str


class HistoryResponse(BaseModel):
    resp_id: str
    messages: list[dict]
