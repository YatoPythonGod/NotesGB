from abc import ABC, abstractmethod


class BasicCommand(ABC):

    def __init__(self, journal, view):
        self.view = view
        self.journal = journal

    @abstractmethod
    def execute(self):
        pass
