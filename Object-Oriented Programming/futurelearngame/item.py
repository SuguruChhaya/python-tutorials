
#*I will learn how to integrate this in week 4
class Item():
    def __init__(self, name):
        self.name = name
        self.description = None

    
    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        print(f"A {self.name} is there!")
        print(self.description)

    
