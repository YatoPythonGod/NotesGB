import os
import json
from Core.Note import Note


class Importer:
    def __init__(self, journal):
        self.journal = journal

    def import_from(self, file_name):
        if not os.path.exists('Transfer\\Export\\' + file_name):
            return 1

        with open('Transfer\\Export\\' + file_name, 'r') as file:
            load_journal = json.load(file)
            if load_journal:
                id_notes = set(note.get_id() for note in self.journal.get_journal())
                for note in load_journal:
                    if note["_Note__id"] in id_notes:
                        continue
                    tmp = Note(note["_Note__title"], note["_Note__msg"])
                    tmp.set_datetime(note["_Note__datetime"])
                    tmp.set_editing_date(note["_Note__editing_date"])
                    tmp.set_id(note["_Note__id"])
                    self.journal.append(tmp)
                self.journal.sort()
            else:
                return 2

        return 0
