"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

a = float(input("Gimme a number: "))
b = float(input("Gimme a number: "))

i = input("Is one of the numbers a hypothenuse of a right traingle (y/n): ")

if i == 'y':
    print(f"The missing side is {round(math.sqrt(max(a, b)**2 - min(a, b)**2), 1)}.")
else: 
    print("ok")