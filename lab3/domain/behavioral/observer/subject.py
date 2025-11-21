from typing import List
from .observer import Observer


class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event_type: str, data: dict) -> None:
        for obs in self._observers:
            obs.update(event_type, data)
