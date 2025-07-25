from abc import ABC, abstractmethod

from crypto_a2a.server.agent_execution import RequestContext
from crypto_a2a.types import MessageSendParams, Task


class RequestContextBuilder(ABC):
    """Builds request context to be supplied to agent executor"""

    @abstractmethod
    async def build(
        self,
        params: MessageSendParams | None = None,
        task_id: str | None = None,
        context_id: str | None = None,
        task: Task | None = None,
    ) -> RequestContext:
        pass
