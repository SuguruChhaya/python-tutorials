
#*This file will contain static and class methods and all.
class RPGInfo():

    author = "Anonymous"
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print(f"Welcome to {self.title}")

    @staticmethod
    def info():
        print("Made using the OOP RPG creator")

    @classmethod
    def show_author(cls):
        #*Has access to class variables
        print(f'Created by {cls.author}')

    