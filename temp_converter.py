"""
Celsius to Fahrenheit App
This is a console app that
1 - Allow users to enter a number as temperature in Celsius
2 - Makes sure what user entered is valid
3 - Prints the temperature in Fahrenherit
"""

def convertStrToNumber(str):
    try:
        value = int(str)
        return  value
    except ValueError:
        try:
            value = float(str)
            return value
        except ValueError:
             print("The value you have inputed is invalid. Please try again!") 
src = ''

while src != 'q':
    src = input("Enter Temperature in °C (q to quit): ")
    if src != 'q':
        tempC = convertStrToNumber(src) # We can check input is digit or not by using src.isdigit()
        if tempC != None:
            tempF = (tempC * 9/5) + 32
            tempK = tempC + 273.15
            print(tempC,"°C equals to ",tempF,"°F and ",tempK,"°K")

