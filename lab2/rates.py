# File: register.py
# Author: Braden Morrison
# Date: 06/20/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 


print('Welcome to the Libary Management App.')
print('Membership rates')
print()

num_days = int(input("Enter the membership number of days: "))
weeks = (num_days % 4) + 1
week_rate =  10 * weeks * 1.0825
print('Weekly membership: ', weeks, ' weeks at $', round(week_rate,2), sep= '')
