from AbcCommand import BasicCommand


class ShowMenuCommand(BasicCommand):

    def execute(self):
        self.view.show_menu()
