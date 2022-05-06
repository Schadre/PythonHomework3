import math
def Square_Footage(length, width):
    return length * width
length = float(input("Please enter length: "))
width = float(input("Please enter width: "))
area = length + width
Square_Footage(length, width)
print("The Area is: ", area)


def  CircumferenceOfCircle(radius):
    return 2 * math.pi * radius
radius = float(input("Please Enter the radius of a circle: "))

circumference = CircumferenceOfCircle(radius)
print("The Circumference is ", circumference)