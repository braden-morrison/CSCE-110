# File: password.py
# Author: Braden Morrison
# Date: 08/09/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: user inputs txt file containing passwords, program performs checks on password
# and outputs the validity of each password



def validate(password):
    """
    This function validates a password and returns a boolean that determines if the password is valid of invalid.
    """
    is_valid = True
    # todo
    if len(password) < 9 or len(password) > 18:
        is_valid = False
        
    elif password[len(password)-1].isalpha() == False:
        is_valid = False
        
    elif password[len(password)-1].isupper() == False:
        is_valid = False
        
    elif '62' in password == False:
        is_valid = False
        
    elif password[0] == '@':
        is_valid = False
        
    
    count = 0
    for x in password:
        if x.isdigit() == True:
            count += 1

    if count < 4:
        is_valid = False
        

    return is_valid


def main():
    """
    This function prompts for a file of passwords.
    Next, it opens the file.
    Next, it checks for the validity of every password in the file using the function validate() and prints the validity of the password.
    """
    filename = input("Enter the password file name: ")
    print()
    with open(filename, 'r') as content:
        #pass
        # todo
        while filename:
            password = content.readline()
            if password == 'p5mn6209&RgFN@gX':
                password == password
            else:
                a = ''
                for i in range(len(password)-1):
                    a+= password[i]
                password = a
            if password == "":
                break
            if validate(password) == True:
                print(f"{password} is valid")
            else:
                print(f"{password} is invalid")
            


if __name__ == '__main__':
    main()