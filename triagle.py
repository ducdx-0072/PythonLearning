"""
This is a console app that
1 - Allow users to enter two numbers as length of legs
2 - Makes sure what user entered are valid
3 - Calculated and prints the hypotenuse and the area of the triangle
"""
from math import sqrt,pow

def convertStrToNumber(str):
    try:
        value = int(str)
        if value > 0:
            return  value
        else:
            print("The value you have inputed is invalid. Please try again!")
    except ValueError:
        try:
            value = float(str)
            if value > 0:
                return value
            else:
                print("The value you have inputed is invalid. Please try again!")
        except ValueError:
             print("The value you have inputed is invalid. Please try again!")

inp1 = input("Enters the length of leg 1: ")
leg1Length = convertStrToNumber(inp1)
if leg1Length != None:
    inp2 = input("Enters the length of leg 2: ")
    leg2Length = convertStrToNumber(inp2)
    if leg2Length != None:
        #Calculate length of leg 3
        leg3Length = sqrt(pow(leg1Length,2) + pow(leg2Length,2))
        print("Length of the hypotenuse is: ", leg3Length)
        area = leg1Length*leg2Length/2
        print("Area of the triangle is: ", area)
