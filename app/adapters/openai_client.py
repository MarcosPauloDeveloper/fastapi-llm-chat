from openai import OpenAI, APIError, RateLimitError
from app.core.config import settings


class OpenAIClient:
    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.client = OpenAI(api_key=api_key or settings.OPENAI_API_KEY)
        self.model = model or settings.MODEL

    def respond(self, context: list[dict]) -> tuple[str, list[dict]]:
        try:
            resp = self.client.responses.create(
                model=self.model,
                input=context,
            )
            context += resp.output
            return resp.output_text, context, resp.id
        except RateLimitError as e:
            raise RuntimeError("OpenAI rate limit exceeded") from e
        except APIError as e:
            raise RuntimeError(f"OpenAI API error: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Unexpected error from OpenAI: {e}") from e
