from const import NAMES_MAP, REPLIES_LIST
from random import choice


class Handler:
    @staticmethod
    def name_parser(message):
        names = list(NAMES_MAP.keys())
        for name in names:
            if name in message.lower():
                return dict(name=name, message=choice(NAMES_MAP[name]), reply=choice(REPLIES_LIST))


