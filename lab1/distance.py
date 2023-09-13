# File: distance.py
# Author: Braden Morrison
# Date: 06/10/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: asks for 2 coordinate pts, calculates then prints their distance



x1 = float(input("x coordinate of the first point: "))
y1 = float(input("y coordinate of the first point: "))
print()
x2 = float(input("x coordinate of the second point: "))
y2 = float(input("y coordinate of the second point: "))
print()

distance = float((((x1-x2)**2) + ((y1-y2)**2))**0.5)

print('The distance between points (', x1, ', ', y1, ') and (', x2, ', ', y2, ') is ', round(distance,2), sep='')
