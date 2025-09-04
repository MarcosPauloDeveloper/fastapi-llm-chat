from collections import defaultdict


class InMemoryContextStore:
    def __init__(self):
        self._ctx = defaultdict(list)

    def get_context(self, resp_id: str) -> list[dict]:
        return self._ctx.get(resp_id, [])

    def set_context(self, resp_id: str, ctx: list[dict]):
        self._ctx[resp_id] = ctx

    def clear(self, resp_id: str):
        self._ctx.pop(resp_id, None)
