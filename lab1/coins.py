# File: coin.py
# Author: Braden Morrison
# Date: 06/10/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: asks for dollar amt, calculates change of different coins



amt = float(input("Please enter the dollar amount: "))
halves = int(amt/.50)
quarters = int(amt/.25)
dimes = int(amt/.1)
print()
print('For $', amt, ', you can get ', halves, ' halves, or ', quarters, ' quarters, or ', dimes, ' dimes.', sep='')
