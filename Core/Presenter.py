from Commands.AddNoteCommand import AddNoteCommand
from Commands.DelNoteCommand import DelNoteCommand
from Commands.EditNoteCommand import EditNoteCommand
from Commands.ShowJournalCommand import ShowJournalCommand
from Commands.ImportCommand import ImportCommand
from Commands.ExportCommand import ExportCommand
from Commands.ShowMenuCommand import ShowMenuCommand
from Commands.ExitCommand import ExitCommand


class Presenter:
    def __init__(self, journal, view):
        self.journal = journal
        self.view = view
        self.commands = {1: AddNoteCommand(self.journal, self.view),
                         2: DelNoteCommand(self.journal, self.view),
                         3: EditNoteCommand(self.journal, self.view),
                         4: ShowJournalCommand(self.journal, self.view),
                         5: ExportCommand(self.journal, self.view),
                         6: ImportCommand(self.journal, self.view),
                         7: ShowMenuCommand(self.journal, self.view),
                         8: ExitCommand(self.journal, self.view),
                         }

    def run(self):
        user_choice = 0
        while user_choice != 8:
            self.commands[7].execute()
            user_choice = self.view.get_int()
            if not user_choice or 0 > user_choice or user_choice > 8:
                self.view.get_msg("Invalid number!")
                continue
            self.commands[user_choice].execute()

