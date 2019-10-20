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

    async def handler(self, payload):
        message = payload.decode('utf-8')
        if message == 'ON':
            await self.set_state(1)
        elif message == 'OFF':
            await self.set_state(0)
