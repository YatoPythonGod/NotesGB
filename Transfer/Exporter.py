import json
import os


class Exporter:
    def __init__(self, journal):
        self.journal = journal

    def export_to(self, file_name):
        if not os.path.exists('Transfer\\Export'):
            os.makedirs('Transfer\\Export')

        filename = os.path.join('Transfer\\Export', file_name)
        json_dict = [note.__dict__ for note in self.journal.get_journal()]

        with open(filename, 'w') as file:
            file.write(json.dumps(json_dict))
