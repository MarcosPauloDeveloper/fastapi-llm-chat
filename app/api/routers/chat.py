from fastapi import APIRouter, Depends, HTTPException
from app.use_case.chat_use_case import ChatUseCase
from app.schemas.chat import ChatRequest, ChatResponse
from app.api.deps.dep import get_chat_uc

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest, uc: ChatUseCase = Depends(get_chat_uc)):
    try:
        reply, resp_id = uc.handle_message(payload.resp_id, payload.message)
        return ChatResponse(reply=reply, id=resp_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
