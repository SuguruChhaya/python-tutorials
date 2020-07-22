from character import Character
from character import Enemy

dave = Character("Dave", "A smelly zombie!")
dave.describe()
dave.set_conversation("Hi!!")
dave.talk()

#*I am going to create the enemy zombie, bob
bob = Enemy("Bob", "A dangerous zombie!")
bob.describe()
fight_with = input("What will you fight bob with?")
bob.set_weakness("cheese")
bob.fight(fight_with)