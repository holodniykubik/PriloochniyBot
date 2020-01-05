from random import choice


class Randomizer:
    def __init__(self, users_list):
        self.users_list = users_list

    def choose_pidor(self):
        return choice(self.users_list)
