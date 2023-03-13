import datetime


class Journal:

    def __init__(self):
        self.__notes = []

    def get_journal(self):
        return self.__notes

    def get_note(self, index):
        if 0 <= index < len(self.__notes):
            return self.__notes[index]

    def size(self):
        return len(self.__notes)

    def sort(self, func=lambda x: x.get_editing_date() if x.get_editing_date() else x.get_datetime()):
        self.__notes.sort(key=func)

    def append(self, note):
        self.__notes.append(note)

    def remove(self, index):
        if 0 <= index < len(self.__notes):
            self.__notes.pop(index)
            return True
        return False

    def edit_note(self, index, title, msg):
        note = self.get_note(index - 1)
        if note:
            note.set_title(title)
            note.set_msg(msg)
            note.set_editing_date(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
            self.remove(index - 1)
            self.append(note)
            return True
        return False
