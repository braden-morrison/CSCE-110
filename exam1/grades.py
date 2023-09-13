# File: grades.py
# Author: Braden Morrison
# Date: 06/22/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 

first_name = input("First name: ")
last_name = input("Last name: ")
num_grades = int(input("Number of grades: "))
avg = 0.00
grade = ''
for x in range(num_grades):
    print('Enter grade ', x + 1, ': ', sep= '', end= ' ')
    grade = float(input())
    avg += grade

avg = avg / num_grades
avg = round(avg,2)

if avg / 100 < 0.00 or avg / 100 > 1.00:
    grade = 'Z'
elif avg / 100 >= .9:
    grade = 'A'
elif avg / 100 >= .8:
    grade = 'B'
elif avg / 100 >= .7:
    grade = 'C'
elif avg / 100 >= .6:
    grade = 'D'
elif avg / 100 < .6:
    grade = 'F'

print()
print('Student name:', first_name.capitalize(), last_name.capitalize())
print('Average grade:', avg)
if grade != 'Z':
    print('Letter grade:', grade)
else:
    print('Invalid grade')

