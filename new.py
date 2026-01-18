a=int(input("Enter the first number:"))
b=int(input("enter the second number:"))
if a==b:
    print("the numbers are equal")
else:
    print("the numbers are not equal")
    
m=int(input("enter the first number:"))
n=int(input("enter the second number:"))
if m>n:
    print("m is greater")
elif n>m:
    print("n is greater")
else:
    print(" both are equals")
a=int(input("Enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number"))
if (a<b and b<c):
    print("a is minimum")
elif (b<a and b<c):
        print("b is minimum")
else:
    print("c is minimum")

maths=int(input("Enter the maths marks:"))
English=int(input("enter the English marks:"))
Hindi=int(input("enter the Hindi"))
if maths>=40:
    print("pass")
else:
    print("fail")
if English>=40:
    print("pass")
else:
    print("fail")
if Hindi>=40:
    print("pass")
else:
    print("fail")

a=int(input("enter the age of the person:"))
if a>=18:
    print("a is eligible for voting ")
else:
    print("not eligible for voting")
m=int(input("enter the marks of maths:"))
s=int(input("enter the marks of science:"))
if m>=40 and s>=40:
    print("pass in both subjects")
elif m>=40 and s<40:
    print("pass in maths and fail in science")
elif m<40 and s>=40:
    print("pass in science but fail in maths")
else:
    print("fail in both subjects")
p=int(input("enter the purchase amount:"))
m=bool(input("do you have membership:"))
if p>=1000 or True:
    print("eligible for discount")
elif p>=1000 or False:
    print("eligible for discount")
elif p<1000 or True:
    print("eligible for discount")
else:
    print("not eligible for discount")
m=int(input("enter the marks of the student:"))
if m>=90:
    print("A")
elif m>=80 and m<90:
    print("B")
elif m>=70 and m<80:
    print("C")
else:
    print("Fail")   
y=int(input("enter the year:"))
if y%4==0:
    print("Leap year") 
else:
    print("Not leap year")
d=int(input("enter the no of day:"))
if d==1:
    print("sunday")
elif d==2:
    print("monday")
elif d==3:
    print("Tuesday")
elif d==4:
    print("Wednesday")
elif d==5:
    print("Thrusday")
elif d==6:
    print("Friday")
else:
    print("Saturday")

T=int(input("enter the temperature:"))
if T<0:
    print("freezing")
elif T>0 and T<20:
    print("cold")
elif T>21 and T<35:
    print("warm")
else:
    print("Hot")
n=int(input("enter the number:"))
list=[5,3,6,9,8]
print(list[0])
print(list[4])
print(len(list))
listt=[6,39,5,99,65,66,78]
a=sum(listt)
print(a)
liist=[apple,orange,banana,mango,grapes]
liist.append()=guava
print(liist)
list=[5,6,3,9,4,6,8]
list.remove(6)
print(list)
list.pop(4)
print(list)
list=[3,2,6,9,6,7,4,6,7]
print(list.count(6))
list=[5,3,6,9,6,4,5,2,6]
if 4 in list:
    print("founded")
else:
    print("not founded")
list=[5,6,9,7,8]
print(list.index(9))
    
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def print_details(self):
            print(f"Name: {self.name}")
            print(f"Age:{self.age}")
    Student1=Student("sonu",50)
    Student1.print_details()

class Employee:
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def print_details(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")
    Employee1=Employee("Kunal",5000)
        
class Mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
        def print_details(self):
            print(f"Brand:{self.brand}")
            print(f"Model{seld.model}")
            
            Mobile1=Mobile("Samsung","s24")
        
















