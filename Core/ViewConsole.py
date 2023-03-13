from View import View


class ViewConsole(View):

    def show_menu(self):
        print(
            """
1. Add note in jornal
2. Delete a note from the journal  
3. Edit a note
4. Show journal
5. Export
6. Import
7. Show menu
8. Exit
            """)

    def get_command(self, message):
        return int(input(message))

    def get_str(self, message):
        return input(message)

    def get_int(self, message="Please enter number: "):
        tmp = input(message)
        if tmp.isdigit():
            return int(tmp)

    def get_msg(self, message):
        print(message)

    def show_journal(self, journal):
        if journal.size() == 0:
            print("Journal is empty")
            return
        for i, note in enumerate(journal.get_journal(), start=1):
            print(f"\n{i}.\nTittle: {note.get_title()}\nDate of creation: {note.get_datetime()}")
            if note.get_editing_date():
                print(f"Last modified date: {note.get_editing_date()}")
            print(f"Message: {note.get_msg()}")
