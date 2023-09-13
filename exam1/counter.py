# File: counter.py
# Author: Braden Morrison
# Date: 06/22/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 


input_list = ''
while input_list != 'quit':
    input_list = input("Enter sentence: ")
    if input_list == 'quit':
        print('end')
        break
    else:
        list = input_list.split()
        pali = 0
        non = 0
        for i in list:
            word = str(i)
            if len(word) % 2 == 0:
                x = 0
                valid = bool(0)
                for j in word:
                    d1 = word[x]
                    d2 = word[len(word) - x - 1]
                    if d1.upper() != d2.upper():
                        valid = False
                        break
                    else:
                        valid = True
                    if len(word) / (x + 1) == 2:
                        break
                    x += 1
                if valid == True:
                    pali += 1
                else: 
                    non += 1
            else:
                x = 0
                valid = bool(0)
                for j in word:
                    d1 = word[x]
                    d2 = word[len(word) - x - 1]
                    if d1.upper() != d2.upper():
                        valid = False
                        break
                    else:
                        valid = True
                    if len(word) / (x + 2) < 2:
                        break
                    x += 1
                if valid == True:
                    pali += 1
                else: 
                    non += 1

        print('Found', pali, 'palindromes and', non, 'non-palindromes.')
        print()


