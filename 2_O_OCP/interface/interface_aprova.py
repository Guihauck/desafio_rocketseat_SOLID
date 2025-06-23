from abc import ABC, abstractmethod

class AprovacaoExame(ABC):
    @abstractmethod
    def aprovar(self, exame):
        pass