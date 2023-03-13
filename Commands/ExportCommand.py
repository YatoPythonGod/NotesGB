from AbcCommand import BasicCommand
from Transfer.Exporter import Exporter


class ExportCommand(BasicCommand):

    def execute(self):
        if self.journal.size() == 0:
            print("Journal is empty")
            return

        exp = Exporter(self.journal)
        file_name = self.view.get_str("Enter the name of the file to export: ")
        while len(file_name) < 1:
            self.view.get_msg("Invalid file name")
            file_name = self.view.get_str("Enter the name of the file to import:")

        exp.export_to(file_name + ".json")
