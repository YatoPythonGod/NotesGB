from AbcCommand import BasicCommand
from Core.Note import Note


class AddNoteCommand(BasicCommand):

    def execute(self):
        title = self.view.get_str("Please enter a title for this note: ")
        while len(title) == 0:
            self.view.get_msg("Invalid title!")
            title = self.view.get_str("Please enter a title for this note: ")

        msg = self.view.get_str("Please enter a title for this note: ")
        while len(msg) == 0:
            self.view.get_msg("Invalid message!")
            msg = self.view.get_str("Please enter a title for this note: ")

        self.journal.append(Note(title, msg))
        self.view.get_msg("Done!")
