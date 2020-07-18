# MODIFY the function to catch exceptions
'''
def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a,2))



# Potential IndexError
print(invert_at_index(a, 5))
'''
# *Can create custom errors


class SalaryError(ValueError):
    pass


class BonusError(SalaryError):
    pass


class Employee:
    MIN_SALARY = 30000
    MAX_RAISE = 5000

    def __init__(self, name, salary=30000):
        self.name = name
    # If salary is too low
        if salary < Employee.MIN_SALARY:
            # Raise a SalaryError exception
            raise SalaryError("Salary is too low!")
        self.salary = salary

    def give_bonus(self, amount):
        if amount > Employee.MAX_RAISE:
            raise BonusError("Bonus amount is too high!")
        elif self.salary + amount < Employee.MIN_SALARY:
            raise BonusError("Salary after bonus is too low!")


#!If I run the next line, I will get a salary error or bonus error
#unpaid = Employee("dumb", 1)
too_much = Employee("Suguru", 50000)
# too_much.give_bonus(50000)
minimum = Employee("Akashi", 30000)
# minimum.give_bonus(-1000)

# ?Interestingly, the parent class with catch the errors from its subclass
# *If I run this, the parent class (SalaryError) will catch the Bonuserrors too
try:
    minimum.give_bonus(50000)
except SalaryError:
    print("Salary Error caught!!")

#!On the otherhand, the subclass doesn't catch errors with the parent class
# *So when error checking, listing the sub-class error first gives a better description of the error
try:
    unpaid = Employee("Unpaid", 0)
except BonusError:
    print("SalaryError caught!!")
