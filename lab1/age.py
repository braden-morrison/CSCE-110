# File: age.py
# Author: Braden Morrison
# Date: 06/10/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: asks for personal info, displays info and age in 5 years



name1 = input("What is your first name? ")
name2 = input("What is your last name? ")
title = input("Which title do you prefer? Mr., Mrs., Miss, Ms., Dr.: ")
year = int(input("In what year were you born? "))
print()
age = (2023 - year) + 5
print ('Welcome, ', title, ' ', name1, ' ', name2, '.\nYou will be ', age, ' years old in five years.', sep='')