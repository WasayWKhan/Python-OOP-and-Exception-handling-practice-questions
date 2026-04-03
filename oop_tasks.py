# =========================================
# AI Internship - OOP & Exception Handling
# =========================================

print("\n--- Task 1: Student Class ---")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name, "| Marks:", self.marks)

s1 = Student("Wasay", 92)
s2 = Student("Ayaan", 85)
s1.display()
s2.display()


print("\n--- Task 2: Laptop Class ---")

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("Dell", 75000)
print(l1.brand, l1.price)


print("\n--- Task 3: Rectangle Area ---")

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

r = Rectangle(12, 8)
print("Area:", r.area())


print("\n--- Task 4: Employee Class ---")

class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

e = Employee("Wasay")
print(e.name, "-", Employee.company_name)


print("\n--- Task 5: Static Method ---")

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print("Sum:", Calculator.add(45, 55))


print("\n--- Task 6: Inheritance Override ---")

class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()


print("\n--- Task 7: Multilevel Inheritance ---")

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept

m = Manager("Wasay", 101, "AI")
print(m.name, m.emp_id, m.dept)


print("\n--- Task 8: Multiple Inheritance ---")

class Father:
    def showFather(self):
        print("Father: Ahmed")

class Mother:
    def showMother(self):
        print("Mother: Sara")

class Child(Father, Mother):
    pass

ch = Child()
ch.showFather()
ch.showMother()


print("\n--- Task 9: Method Overriding ---")

class BankAccount:
    def withdraw(self, amount):
        print("Withdraw:", amount)

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Withdraw with minimum balance check:", amount)

s = SavingsAccount()
s.withdraw(5000)


print("\n--- Task 10: Encapsulation ---")

class Account:
    def __init__(self):
        self.__balance = 10000

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        self.__balance -= amt

    def show(self):
        print("Balance:", self.__balance)

a = Account()
a.deposit(2000)
a.withdraw(1500)
a.show()


print("\n--- Task 11: Polymorphism ---")

class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 6 * 6

shapes = [Circle(), Square()]

for s in shapes:
    print("Area:", s.area())


print("\n--- Task 12: Abstract Class ---")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike starts")

class Car(Vehicle):
    def start(self):
        print("Car starts")

Bike().start()
Car().start()


print("\n--- Task 13: Division Handling ---")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")


print("\n--- Task 14: Invalid Input ---")

try:
    x = int("abc")
except ValueError:
    print("Invalid input")


print("\n--- Task 15: Calculator Exception ---")

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Value error")


print("\n--- Task 16: File Handling ---")

try:
    f = open("test.txt", "w")
    f.write("Hello AI")
finally:
    f.close()
    print("File closed")


print("\n--- Task 17: Custom Exception ---")

class InsufficientBalanceError(Exception):
    pass

balance = 500

try:
    withdraw = 600
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance")
except InsufficientBalanceError as e:
    print(e)


print("\n--- Task 18: Voting Eligibility ---")

try:
    age = 16
    if age < 18:
        raise Exception("Not eligible to vote")
except Exception as e:
    print(e)


print("\n--- Task 19: Index Error ---")

lst = [10, 20, 30]

try:
    print(lst[5])
except IndexError:
    print("Index out of range")


print("\n--- Task 20: Try-Except-Else ---")

try:
    x = 20
    y = 5
    result = x / y
except Exception:
    print("Error")
else:
    print("Result:", result)


print("\n--- Task 21: ML vs DL ---")

print("Machine Learning: Uses algorithms like Linear Regression, Decision Trees")
print("Deep Learning: Uses Neural Networks like CNN, RNN")
