# File: password.py
# Author: Braden Morrison
# Date: 06/20/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 


print('Welcome to the library Management App.')
print('Password generation')



last_name = input("Enter the member's last name: ")
phone = input("Enter the member’s phone number: ")
address = input("Enter the member’s mailing address: ")

p1 = last_name.count('a')
p1_1 = last_name.count('e')
p1_2 = last_name.count('i')
p1_3 = last_name.count('o')
p1_4 = last_name.count('u')
A1 = str(p1 + p1_1 + p1_2 + p1_3 + p1_4)

first_digit = phone[0]
last_letter = last_name[-1].upper()
A2 = phone.replace(first_digit, last_letter)

zip_code = address.split()[-1]
A3 = zip_code[-4:][::-1]

street_number = address.split()[0]

for digit in street_number:
    if int(digit) % 2 == 0:
        street_number = street_number.replace(digit,"0")
        #d = int(digit)
        #street_number[d] = '0'
    else:
        street_number = street_number.replace(digit,"1")
        #c = int(digit)
        #street_number[c] = '1'
A4 = street_number

All = A1 + A2 + A3 + A4

print('Generated password:', All)