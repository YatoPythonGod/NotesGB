from AbcCommand import BasicCommand


class ShowJournalCommand(BasicCommand):

    def execute(self):
        self.view.show_journal(self.journal)

