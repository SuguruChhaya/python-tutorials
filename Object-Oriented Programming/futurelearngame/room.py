class Room():
    #*Need constructor
    NUM_ROOMS = 0
    def __init__(self, room_name):
        #*Instead of defining a variable in other methods, I can set them in the constructor using none.
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        #*In order to add characters in the room, I need to add them into the Room class
        self.character = None
        Room.NUM_ROOMS += 1

    #*I am going to create a getter and setter method.
    def set_description(self, description):
        self.description = description

    @staticmethod
    #*Static methods can be used without making instances. It can be used outside the class whenever.
    def print_random():
        print("This is what a static method can do.")

    
    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character =new_character
    
    def destroy_character(self):
        self.character = None
    
    def get_character(self):
        return self.character


    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        direction_list = ["north", 'south', 'east', 'west']

        #*Try linking the opposite too in one shot instead of reassigning all the time
        for item in range(0, 4):
            if direction_list[item] == direction:
                if item == 0 or item == 2:
                    opposite = direction_list[item + 1]
                else:
                    opposite = direction_list[item - 1]

        self.linked_rooms[direction] = room_to_link
        room_to_link.linked_rooms[opposite] = self

    def get_details(self):
        print(f"The {self.name}")
        print("-------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")

    #*Move between rooms
    def move(self, direction):
        if direction in self.linked_rooms:
            #*For both return statements, the room we are currently in is returned
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self

