# *How to let python know that objects with the same instance attributes are equal:
class Equal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #!By defining the __eq__ function, we can compare whether objects have same instance attributes.
    # * The first object is assigned to "self" and the second one to "other"
    #!To check whether two objects belong in the same class, I can find whether their type is the same.

    def __eq__(self, other):
        return type(self) == type(other) and (self.name == other.name) and (self.age == other.age)

    def __gt__(self, other):
        return (self.name > other.name) and (self.age > other.age)


a = Equal("John", 40)
b = Equal("John", 40)
c = Equal("Zack", 50)

print(a == b)
print(c > a)


class Fake():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name == other.name) and (self.age == other.age)


d = Fake("John", 40)
#!Even though a and d belong to different classes, since their values are same, python recognizes them as equal.
print(a == d)

# *As you can see, python recognizes classes and its subclasses equal by default.
# *the child's __eq__ is always called
#!To avoid this, I can check whther they belong in the same class


class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return type(self) == type(other)


class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return type(self) == type(other)


ab = Parent()
bc = Child()
print(bc == ab)
