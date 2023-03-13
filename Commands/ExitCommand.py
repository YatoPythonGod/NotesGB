from AbcCommand import BasicCommand


class ExitCommand(BasicCommand):

    def execute(self):
        self.view.get_msg("See you later!")
