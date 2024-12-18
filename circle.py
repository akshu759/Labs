#WAP to get area of circle 
import math 

def calculate_area_of_circle(radius):
    area= math.pi*radius*radius
    return area

radius= float(input("Enter the radius of the circle:"))

area= calculate_area_of_circle(radius)

print(f"The area pf the circle is:{area}")