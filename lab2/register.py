# File: register.py
# Author: Braden Morrison
# Date: 06/20/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 

import re

print('Welcome to the Library Management App.')
print('Member registration')
first_name = input("Enter the member’s first name: ")
middle_name = input("Enter the member’s middle name: ")
last_name = input("Enter the member’s last name: ")
phone = input("Enter the member’s phone number: ")
address = input("Enter the member’s mailing address: ")
print()
street, city, state_zip = [part.strip() for part in address.split(',')]
street_number, street_name = street.split(' ', 1)
state, zip = state_zip.split()
phone2 = re.sub(r'\D', '', phone)
p1 = phone2[0:3]
p2 = phone2[3:6]
p3 = phone2[6:10]

print('Member name:', first_name.capitalize(), middle_name.capitalize(), last_name.capitalize())
print("Phone number (International format): +1-", p1, "-", p2, "-", p3, sep= '')
print("Phone number (North American format): (", p1, ") ", p2, "-", p3, sep= '')
print("Phone number (Local format): ", p2, ".", p3, sep= '')
print('Street number:', street_number)
print('Street name:', street_name.upper())
print('City:', city.upper())
print('State:', state)
print('Zip:', zip)