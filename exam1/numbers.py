# File: numbers.py
# Author: Braden Morrison
# Date: 06/22/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 


input_list = input("Enter numbers: ")
list = input_list.split()
list = [int(i) for i in list]
length = len(list)
even = 0
odd = 0
for i in list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
min = min(list)
max = max(list)
sum = sum(list)

print('Count of numbers:', length)
print('Even numbers:', even)
print('Odd numbers:', odd)
print('Sum of numbers:', sum)
print('Highest number:', max)
print('Lowest number:', min)

