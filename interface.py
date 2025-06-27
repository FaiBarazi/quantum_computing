import qutip
from abc import ABC, ABCMeta, abstractmethod
from contextlib import contextmanager


class Qubit(metclass=ABCMeta):
    @abstractmethod
    def h(self):
        pass

    @abstractmethod
    def measure(self) -> bool:
        pass

    @abstractmethod
    def reset(self):
        pass


class QuantumDevice(metaclass=ABCMeta):
    @abstractmethod
    def allocate_qubit(self) -> Qubit:
        pass

    @abstractmethod
    def deallocate_qubit(self, qubit: Qubit):
        pass

    @contextmanager
    def using_qubit(self):
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()
            self.deallocate_qubit(qubit)
