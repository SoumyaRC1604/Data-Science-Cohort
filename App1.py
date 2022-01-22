'''character_name = "Tom"
character_age = "35"
is_male = True
print("There is a man named " + character_name + ", ")
print("He is "+ character_age + " years old")
phrase = "giraffe academy"
print(phrase.index("g"))
print(len(phrase))
print(phrase.replace("giraffe", "elephant"))
print(phrase.upper())
print(phrase.lower().islower())
print(-2.0987)
print(2+3.5)
print(10%3)
my_num = -5
print(my_num)
print(str(my_num) + " is my favorite number")
print(abs(my_num))
print(pow(3,2))
print(max(4,6))
print(round(3.7))
from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))'''
#Inheritance
from Chef import Chef
from ChineseChef import ChineseChef
myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()