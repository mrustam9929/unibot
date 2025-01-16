from abc import ABC, abstractmethod


class BaseBotModule(ABC):
    @abstractmethod
    def register_handlers(self, bot):
        raise NotImplementedError
