from abc import ABC, abstractmethod


class Accessory(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_state(self, state: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_state(self) -> int:
        raise NotImplementedError()

    def handler(self, payload):
        if payload == 'ON':
            self.set_state(1)
        elif payload == 'OFF':
            self.set_state(0)
