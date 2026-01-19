class Animal:
    def speak(self):
        print("animals make sound")
class Dog(Animal):
    def bark(self):
        print("dog barks!")
        d=Dog()
        d.speak()
        d.bark()

class BankAccount:
    def __init__(self,owner,balance):
        self.owner =owner
        self.__balance+=balance
        
    def deposit(self,amount):
        self.__balance+=amount
        
    def get_balance(self):
        return self.__balance
    
acc=BankAccount("Alice",10000)
acc.deposit(5000)
print(acc.get_balance())

class Students:
    def __init__(self, name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f"Name: {self.name}")
        print(f"roll_no: {self.roll_no}")
        print(f"Name: {self.marks}")
import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
            
    def calculate_area(self):
     area = math.pi * self.radius * self.radius
     return area
     
    def calculate_circumference(self):
        circumference = 2*math.pi * self.radius
        return circumference

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
        

class Vahicle:
    def start(self):
        self.start=start


class Grandfather:
    def show(self):
        print("Grandfather")
class Father(Grandfather):
    def show(self):
        print("Father")
        super().show()
class Son(Father):
    def show(self):
        print("Son")
        super().show()
        
print(Son.mro())
print(Father.mro()) 
print(Grandfather.mro())      


    
        
        
        
        