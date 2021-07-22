#1. Print + string
from typing import SupportsBytes


print("Hello World!")

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

char_name = "john"
char_age = "80"

print("There once was a man named " + char_name + ",")
print("he was " + char_age + " years old.")
print("He really liked the name " + char_name + ",")
print("but didn't like being " + char_age + ".")

phrase = "It's really hard to start with something but when you get going it becomes a lot easier."
print(phrase.lower())
print(phrase.upper())
#Can also add islower and isupper, len(phrase), phrase[num], .index("something"), .replace("hard", "easy").

name = input("Please enter your name: ")
age = input("Please enter your age: ")
print("Hello " + name + "! You are" + age + " years old.")

#2. Nums, Basic math equations
num1 = 5
num2 = 35
#all basic math equations + - * / etc.
print(pow(num1, 3))
print(max(num1, num2))
print(round(51.6864684654))

from math import * #Usually import modules at the top
print(floor(3.84)) #round down
print(ceil(46.5325)) #round up
print(sqrt(36)) #square root
#A lot more math functions but these are basics

