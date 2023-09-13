
import math

radius = float(input("Radius of the cone: "))
height = float(input("Height of the cone: "))
volumne = (math.pi * (radius**2) * height) / 3
slant = ((radius**2) + (height**2))**(1/2)
sa = (math.pi * radius * (slant)) + (math.pi * (radius**2))
print('Volume:', round(volumne,2))
print('Slant height:', round(slant,2))
print('Surface:', round(sa,2))