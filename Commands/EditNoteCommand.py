from AbcCommand import BasicCommand


class EditNoteCommand(BasicCommand):

    def execute(self):
        if self.journal.size() == 0:
            print("Journal is empty")
            return

        index = self.view.get_int("Please enter the note number: ")
        if index:
            if 0 < index < self.journal.size():
                title = self.view.get_str("Please enter new title for this note: ")
                while len(title) == 0:
                    self.view.get_msg("Invalid title!")
                    title = self.view.get_str("Please enter a new title for this note: ")

                msg = self.view.get_str("Please enter a message for this note: ")
                while len(msg) == 0:
                    self.view.get_msg("Invalid message!")
                    msg = self.view.get_str("Please enter a title for this note: ")
                tmp = self.journal.edit_note(index, title, msg)
                self.view.get_msg("Done!")
            else:
                self.view.get_msg("Invalid number!")
        else:
            self.view.get_msg("Invalid number!")
