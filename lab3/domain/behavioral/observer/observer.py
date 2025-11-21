from abc import ABC, abstractmethod
from typing import Any, Dict


class Observer(ABC):

    @abstractmethod
    def update(self, event_type: str, data: Dict[str, Any]) -> None:
        ...
