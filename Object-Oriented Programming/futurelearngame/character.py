class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.exist = True


    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def dance(self):
        print(f"You danced with {self.name}")


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        #*The super class is the same thing as Character since it is its parent class.
        #Character.__init__()
        self.weakness = None
        self.bribable = None

    def fight(self, combat_item):
        
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {self.weakness}")
            return True
        else:
            print(f"{self.name} crushes you. You die, LOL.")
            return False

    def set_weakness(self, weakness):
        self.weakness = weakness
        return False

    def bribe(self, bribalble):
        self.bribable = bribalble
        if self.bribable == "True":
            print(f"You bribed {self.name}")
        elif bribalble == "False":
            print(f"You cannot bribe {self.name}")
