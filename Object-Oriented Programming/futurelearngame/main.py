from room import Room
from item import Item
from character import Enemy
from character import Friend
from rpginfo import RPGInfo

#*Game name
spooky_castle = RPGInfo("Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "Suguru"
RPGInfo.show_author()

kitchen = Room("kitchen")
#*Somehow the properties aren't working but I guess that is ok
kitchen.description("A place where you cook.")
#*Note that since the attributes are public, I can change them without using a method
'''
kitchen.description = "Changed"
print(kitchen.description)
'''

ballroom = Room("ballroom")
ballroom.description("A place where you dance.")

dining_hall = Room("dining hall")
dining_hall.description("A place where you eat.")

kitchen.link_room(dining_hall, "south")


ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A dangerous zombie!")
dave.set_conversation("Imma eat ur brain")
dave.set_bribe("False")
dave.set_weakness("cheese")
dining_hall.set_character(dave)
dining_hall.get_character()

akashi = Enemy("Akashi", "The monster")
akashi.set_conversation("Yeet")
akashi.set_bribe("True")
akashi.set_weakness("Call mama")
kitchen.set_character(akashi)

sunny = Friend("Sunny", "A nice friend who likes to dance!")
sunny.set_conversation("Do you want to dance?")
ballroom.set_character(sunny)

#*Start in the kitchen
current_room = kitchen

#*Store items in backpack
backpack = []
loop = True
while loop:
    print("\n")
    current_room.get_details()

    #*Check whether there are characters in the room.
    inhabitant = current_room.get_character()

    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
    if command in ['north', 'south', 'east', 'west']:
        current_room = current_room.move(command)

    elif command == "talk" and inhabitant is not None:
        inhabitant.talk()

    elif command == "fight" and inhabitant is not None:
        fight_with = input(f"What would you fight {inhabitant.name} with?: ")
        if not inhabitant.fight(fight_with):
        #*Might want to remove enemy from game now.
            loop = False
        else:
            current_room.destroy_character()
    
    elif command== "bribe" and inhabitant is not None and isinstance(inhabitant, Enemy):
        inhabitant.bribe(inhabitant.bribable)

    elif command == "dance" and inhabitant is not None and isinstance(inhabitant, Friend):
        inhabitant.dance()


            
    

#*Dave is an enemy zombie


