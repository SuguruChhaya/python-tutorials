'''
class Experiment:
    MINIMUM = 18

    def __init__(self, age):
        self.age = age

    @classmethod
    def class_change(cls):
        return cls(29)

    @staticmethod
    def static_change():
        Experiment.MINIMUM = 80

    def __str__(self):
        return(f"I am {self.age} years old")


a = Experiment(50)
print(a.__str__())
a.static_change()
print(a.MINIMUM)
b = a.class_change()
print(b.__str__())
#!When an class attribute is changed by an instance like "b", it will not change for other instances.
b.MINIMUM = 5
print(a.MINIMUM)
#!But when the class attribute is changed through the class, it changes for all instances
Experiment.MINIMUM = 5
print(a.MINIMUM)

#!As you can see, class methods are useful for breaking down data and reusing it in the class.
# ?Static methods don't take a self argument but can change class values.
# *https://www.tutorialspoint.com/class-method-vs-static-method-in-python
# *https://www.geeksforgeeks.org/class-instance-attributes-python/
# *https://www.programiz.com/python-programming/methods/built-in/classmethod
# * https://stackoverflow.com/questions/207000/what-is-the-difference-between-class-and-instance-attributes
'''
'''

class Parent():
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
<<<<<<< HEAD:Tutorials/Object-Oriented Programming/expeirment.py
        #Parent.__init__(self, name)
=======
        Parent.__init__(self, name)
>>>>>>> 6a63e5e9b1511be28c3dcac2599eb72861c1b201:Tutorials/Object-Oriented Programming/experiment.py
        self.age = age


a = Child("Suguru", 5)
<<<<<<< HEAD:Tutorials/Object-Oriented Programming/expeirment.py
print(a.name)
=======
>>>>>>> 6a63e5e9b1511be28c3dcac2599eb72861c1b201:Tutorials/Object-Oriented Programming/experiment.py
print(a.age)
'''
#!When adding new features to a sub-class, you must define all the attributes in the parent class first.
# *You have to have all the arguments for the __init__ method in the sub-class

'''
class Pass():
    MAX_POSITION = 1
    MAX_SPEED = 5


class Sub(Pass):
    MAX_POSITION = 20


a = Sub()
print(a.MAX_POSITION)
print(a.MAX_SPEED)
b = Pass()
print(b.MAX_POSITION)
'''
#!As you can see, class attributes are inherited but can be changed in a sub-class


class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
        # Recall that Python allows multiple variable assignments in one line
        self.year, self.month, self.day = year, month, day

    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and  convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)


class EvenBetterDate(BetterDate):
    @classmethod
    def format_checker(cls, datestr, format):
        if format == "YYYY-MM-DD":
            return BetterDate.from_str(datestr)
        elif format == "MM-DD-YYYY":
            month, day, year = map(int, datestr.split("-"))
            return cls(year, month, day)


class BestDate(EvenBetterDate):
    @classmethod
    def first_cut(cls, datestr):
        first, second, third = datestr.split("-")
        if len(first) == 4 and len(second) == 2 and len(third) == 2:
            return EvenBetterDate.format_checker(datestr, "YYYY-MM-DD")
        elif len(first) == 2 and len(second) == 2 and len(third) == 4:
            return EvenBetterDate.format_checker(datastr, "MM-DD-YYYY")


bd = BetterDate.from_str('2020-04-30')
print(bd.year)
print(bd.month)
print(bd.day)


a = EvenBetterDate.format_checker("2004-08-07", "YYYY-MM-DD")
print(a.year)
b = EvenBetterDate.format_checker("07-08-2004", "MM-DD-YYYY")
print(b.year)

c = BestDate.first_cut("2000-01-01")
print(c.year)

class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True

class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True

a = Parent()
b = Child()
print(a == b)