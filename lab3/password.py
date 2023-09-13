# File: password.py
# Author: Braden Morrison
# Date: 06/20/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: A password, then validates the password


valid = bool(1)
valid2 = bool(1)
while valid2 == True:
    valid = True
    valid2 = True
    password = str(input("Enter a password: "))
    if password == 'quit':
        break
    print()
    print('Password validation')

    print('9 to 18 characters:', end=' ')
    if len(password) >= 9 and len(password) <= 18:
        print('True')
    else:
        print('False')
        valid = False

    print('No spaces:', end=' ')
    space = password.find(' ')
    if space == -1:
        print('True')
    else:
        print('False')
        valid = False

    print('At least 2 digits:', end=' ')
    digit_counter = 0
    for digit in password:
        if digit.isdigit() == True:
            digit_counter += 1
    if digit_counter >= 2:
        print('True')
    else:
        print('False')
        valid = False

    print('At least 4 letters:', end=' ')
    letter_counter = 0
    for letter in password:
        if letter.isalpha() == True:
            letter_counter += 1
    if letter_counter >= 4:
        print('True')
    else:
        print('False')
        valid = False
    

    print('At least 2 vowels:', end=' ')
    vowel_counter = 0
    for letter in password:
        if (letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or 
            letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or 
            letter == 'u' or letter == 'U'):
            vowel_counter += 1
    if vowel_counter >= 2:
        print('True')
    else: 
        print('False')
        valid = False



    print('At least one uppercase letter:', end=' ')
    upper_counter = 0
    for letter in password:
        if letter.isupper() == True:
            upper_counter += 1
    if upper_counter > 0:
        print('True')
    else:
        print('False')
        valid = False

    print('At least one lowercase letter:', end=' ')
    lower_counter = 0
    for letter in password:
        if letter.islower() == True:
            lower_counter += 1
    if lower_counter > 0:
        print('True')
    else:
        print('False')
        valid = False

    print("At least two special characters from ['$', '#', '@', '&']:", end=' ')
    special_counter = 0
    for letter in password:
        if (letter == '$' or letter == '#' or letter == '@' or letter == '&'):
            special_counter += 1
    if special_counter >= 2:
        print('True')
    else:
        print('False')
        valid = False

    print('No two consecutive identical characters:', end=' ')
    valid3 = False
    x = 0
    for letter in password:
        if x + 1 == len(password):
            print('True')
            break
        if password[x] == password[x+1]:
            print('False')
            valid = False
            break
        x += 1
    
    if valid == True:
        print()
        print('Password', password, 'is valid!')
        print('Number of digits:', digit_counter)
        print('Number of vowels:', vowel_counter)
        print('Number of uppercase letters:', upper_counter)
        print('Number of lowercase letters:', lower_counter)
        print('Number of special characters:', special_counter)
        valid2 = False
    else:
        print('Password', password, 'is invalid. Try again.')
        print()


    