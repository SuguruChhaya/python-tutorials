#!Encapsulation is bundling data with code operating on it

# ?Attributes vs methods
# * Every numpy array has a shape. This is an attribute
# * A numpy array can be reshaped by using the .reshape() method. This is behaviour/activity.
# ?Can use help() to find the methods in a class.

#!This is one way to make a salary raising class.
# *Think of classes as a template
#!Note that "I gave raise!!" is printed when performing the .give_raise method
'''
class Salary:
    def __init__(self, salary):
        self.salary = salary

    def give_raise(self, raise_amount):
        self.salary += raise_amount
        print("I gave raise!!")


suguru = Salary(5000)
suguru.give_raise(5000)
print(suguru.salary)
'''

#!More classes:
'''
class MyCounter:
    #!The first function doesn't necessarily have to be "__init". It can be whatever as long as it states the attributes
    #!of the object
    def set_count(self, n):
        self.count = n
    
mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1
print(mc.count)
'''
# ?Creating an empty class is easy
'''
class Empty:
    pass
#*Assign an object
doesnt_matter = Empty()
'''

# *The following is a basic salary example
#!Note that I can declare attributes along the way. I don't need to declare them all in the first function
# ?This is why "set_salary" has a new parameter, "new_salary"
#!BUT, it might be easier to declare them at first if you are going to do so anyways
# *Good to name classes in uppercase in one word
'''
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self, new_salary):
      self.salary = new_salary
  
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)
'''

# *There are some things I have to be careful of while printing a result of a method
#!mon_sal is assigned to emp.monthly_salary() NOT emp.monthly_salary
# ?There is bracket below because monthly_salary is NOT an attribute, bu is a method
#!What we want is a returning value. If so, we use a () to indicate a method/function
'''
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12

    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)
'''

# ?You can also set the defalut value like this:
'''
class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
'''
# *This way, even if I write:
#emp = Employee("Suguru")
# *and miss the "salary argument", I will not get an error.
# * By putting self.salary = salary, emp.salary will give me "0"
#!But if I specify the salary arguement, it won't turn into 0 (which is weird)

# *A simple exercise I did
'''
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def reflect(self, axis):
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
            
pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
'''
# ?Instance-level data vs class-level data
# *Example of instance level data:
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Josh", 1)
emp2 = Employee("Bob", 2)
'''
# *In this case, there is no shared variable across the class. All variables are different and are assigned outside the class.
#!On the other hand, if you define a variable inside the class before __init__, the variable can be used throughout the class.
#!Don't need self for this case.
# ?These variables are called CLASS ATTRIBUTES

# ?Making class methods
#!Class methods are methods in classes which don't contain "self"
# ?A decorator, "@classmethod" is required
# *Main use of class methods are for alternative constructors.
# Write Python code here

# ?This code might be useful...
'''
class sampleclass:
    count = 0     # class attribute

    def increase(self):
        sampleclass.count += 1


# Calling increase() on an object
s1 = sampleclass()
s1.increase()
print(s1.count)

# Calling increase on one more
# object
s2 = sampleclass()
s2.increase()
print(s2.count)

print(sampleclass.count)
'''
#!This code shows how the class attribute, "count" is being updated everytime increase() is called
'''
#?This code keeps track of my movements and location
class Player:

    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position = self.position + steps
        else:
            position = Player.MAX_POSITION

    

       
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
'''
# * This link explains class methods very well: https://www.programiz.com/python-programming/methods/built-in/classmethod
#!This is an example code from Datacamp
'''
class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year,self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
         # Split the string at "-" and  convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)
'''
# ?Here we can see that "from_str" is a connected function with the class. It works together.
#!By having the "cls" argument, the "cls(year, month, day)" returned can be used in the __init__ method later
# *I think I can think of it as a class method breaking the data down, so the __init__ method can read it and do stuff with it.

# *Interesting code
'''
# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, datetime):
        return cls(datetime.year, datetime.month, datetime.day)

# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)
'''

#!An instance is an object created using the class

# *Off-topic
#!Constructors usually point to methods which initialize the attributes of a class to an instance.
# *This usually is done in the __init__ method.
# ?Default constructors vs parameter constructors
# *default constructors don't take an argument in the __init__ method but sets a default value.
# *User input wouldn't matter.
# ?On the other hand, parameter constructors have parameters in their __init__ functions>
# ?The argument taken in matters in creating the attributes.
# *https://www.geeksforgeeks.org/constructors-in-python/

# *Inheritance is making a new class by reusing what an old class had with some added functionality.

'''
class Parent():
    def __init__(self, amount):
        self.amount = amount


dad = Parent(10000)


class Child(Parent):
    pass


me = Child(5000)
print(me.amount)
#?Is ininstance() finds whether the first argument is an instance of the second
#*"me" is an instance of Child, but is also an instance of Parent since the Child class is inherited from the Parent class
#*on the other hand, "dad" is only an instance of Parent, not Child
print(isinstance(me, Child))
print(isinstance(me, Parent))
print(isinstance(dad, Child))
print(isinstance(dad, Parent))
'''
#!Child has the same attributes as Parent does
# *But when you write additional methods in the sub-class, you must add self to the argument.

# *Interesting code which adds bonuses to manager, but not employee
'''

class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=0.05):
        amount += amount * bonus
        Employee.give_raise(self, amount)


mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=0.03)
print(mngr.salary)
'''


#*How to let python know that objects with the same instance attributes are equal:

