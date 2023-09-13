# File: atm.py
# Author: Braden Morrison
# Date: 06/10/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: asks for dollar amt, calculates change via bills


amt = int(input("Please enter the dollar amount: "))
print()
print('Cash withdrawal for $', amt, sep='')
print()
print(f'{"Denomination":<15}{"Number of bills":^20}')

hundreds = int(amt / 100)
amt = amt%100

fiftys = int(amt / 50)
amt = amt%50

twentys = int(amt / 20)
amt %= 20

tens = int(amt / 10)
amt = amt % 10

fives = int(amt / 5)
amt = amt % 5

ones = int(amt / 1)

print(f'{"$100":<15}{hundreds:^20}')
print(f'{"$50":<15}{fiftys:^20}')
print(f'{"$20":<15}{twentys:^20}')
print(f'{"$10":<15}{tens:^20}')
print(f'{"$5":<15}{fives:^20}')
print(f'{"$1":<15}{ones:^20}')

    
    


