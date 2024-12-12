from src.presence import Presence

class Data:
    def __init__(self, name:str, surname:str, presence:Presence):
        self.name = name
        self.surname = surname
        self.presence = presence