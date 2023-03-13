from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def get_command(self, message):
        pass

    @abstractmethod
    def get_str(self, message):
        pass

    @abstractmethod
    def get_int(self, message):
        pass

    @abstractmethod
    def get_msg(self, message):
        pass

    @abstractmethod
    def show_journal(self, journal):
        pass


