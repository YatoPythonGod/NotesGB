import datetime


class Note:
    __id = 0

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.__id += 1
        obj.__id = cls.__id
        return obj

    def __init__(self, title, msg):
        self.__datetime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        self.__editing_date = None
        self.__title = title
        self.__msg = msg

    def get_id(self):
        return self.__id

    def get_datetime(self):
        return self.__datetime

    def get_editing_date(self):
        return self.__editing_date

    def get_title(self):
        return self.__title

    def get_msg(self):
        return self.__msg

    def set_id(self, id):
        self.__id = id

    def set_editing_date(self, date):
        self.__editing_date = date

    def set_datetime(self, date):
        self.__datetime = date

    def set_title(self, title):
        self.__title = title

    def set_msg(self, msg):
        self.__msg = msg

