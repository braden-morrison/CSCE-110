# File: uin.py
# Author: Braden Morrison
# Date: 06/22/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 

valid = bool(0)
checker = 0
while valid == 0:
    uin = input("Enter UIN: ")
    if len(uin) == 9:
        checker += 1
        
    if uin.isdigit() == True:
        checker += 1
        d1 = int(uin[0])
        d2 = int(uin[(len(uin)-1)])
        if d1 - d2 >= 4 or d2 - d1 >= 4:
            checker += 1

    if checker == 3:
        print('Valid UIN')
        break
    else:
        print('Invalid UIN')
        print()
        checker = 0
