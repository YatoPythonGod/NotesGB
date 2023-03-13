from AbcCommand import BasicCommand


class DelNoteCommand(BasicCommand):

    def execute(self):
        if self.journal.size() == 0:
            print("Journal is empty")
            return

        tmp = self.journal.remove(self.view.get_int("Please enter the note number: "))

        if tmp:
            self.view.get_msg("Done!")
        else:
            self.view.get_msg("Invalid number!")
