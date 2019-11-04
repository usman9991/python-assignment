import sys
from datetime import datetime
from math import pi

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")




print (sys.version)



date = datetime.today()
print("Today's date:", date)


r = float(input ('enter radius of a circle :'))
print ("The area of the circle is " + str(pi * r**2))



fname = input("enter your first name ")
lname = input("enter your last name ")

print ("your full name is " + lname +" " + fname)


first = input("enter first number ")
second = input("enter your second number ")
addtion = int(first) + int(second)
print (addtion)


