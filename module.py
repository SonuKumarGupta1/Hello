class Factory:
    def __init__(self,material,zips,pocket):
        self.material=material
        self.zips=zips
        self.pocket=pocket
    def show(self):
        print(f"The material of the bags are {self.material}, {self.zips}, {self.pocket}")
       
gucci=Factory("leather", 5, 2)
dior=Factory("plastic", 4, 3)
print(gucci.material)
print(dior.pocket)
gucci.show()
        
import math
squ=math.sqrt(625)
print(squ)

fac=math.factorial(6)
print(fac)

flor=math.floor(5.6)
print(flor)

cel=math.ceil(6.8)
print(cel)

poww=math.pow(5,3)
print(poww)

abss=math.fabs(-18)
print(abss)

tri=math.sin(90)
print(tri)

trii=math.cos(90)
print(trii)

triii=math.tan(90)
print(triii)

gcdd=math.gcd(36,60)
print(gcdd)

val=math.exp(3)
print(val)

logg=math.log(10,1000)
print(logg)

rad=math.radians(180)
print(rad)

import random

random_num=random.randint(1,10)
print(random_num)

randomm=random.random()
print(randomm)

rando=random.choice([10,20,30,40,50])
print(rando)

ranin=random.randint(10,100)
print(ranin)

dice=random.randint(1,6)
print(dice)

fruit=random.choice(['apple','banana','mango','graps','orange'])
print(fruit)

#create a random password of 8 characters using lowercase alphabet.

import datetime

dandt=datetime.datetime.now()
print(dandt)

datee=datetime.date.today()
print(datee)






















