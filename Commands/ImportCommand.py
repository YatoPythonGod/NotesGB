from AbcCommand import BasicCommand
from Transfer.Importer import Importer


class ImportCommand(BasicCommand):

    def execute(self):
        imp = Importer(self.journal)
        file_name = self.view.get_str("Enter the name of the file to import:") + ".json"
        while len(file_name) < 1:
            self.view.get_msg("Invalid file name")
            file_name = self.view.get_str("Enter the name of the file to import:") + ".json"

        exit_code = imp.import_from(file_name)
        match exit_code:
            case 0:
                self.view.get_msg("Import complete")
                return
            case 1:
                self.view.get_msg("File not found")
                return
            case 2:
                self.view.get_msg("File is empty")
                return
