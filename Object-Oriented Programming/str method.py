class Print():
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return(f" He is {self.age} years old.")
    #*__repr__ is used to replicate the input
    def __repr__(self):
        return (f"Print({self.age})")


# ?__str__ method gives a description of the object when the object is printed
me = Print(5)
print(me)
print(repr(me))
