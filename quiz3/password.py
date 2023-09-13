password = input("Enter password: ")
howdy = 0
print('9 to 18 characters:', end=' ')
if len(password) >= 9 and len(password) <= 18:
    print('True')
    howdy += 1
else:
    print('False')

print('Ends with letter:', end=' ')
index = len(password) - 1
newstring = password[index]
if newstring.isalpha() == 1: 
    print('True')
    howdy += 1
    if newstring.isupper() == 1:
        print('Ends with uppercase letter: True')
        howdy += 1
    else:
        print('Ends with uppercase letter: False')
else:
    print('False')
    print('Ends with uppercase letter: False')


print('Contains 979:', end=' ')
index2 = password.find('979')
if index2 == -1:
    print('False')
else:
    print('True')
    howdy += 1


print('Does not start with @:', end=' ')
if password[0] == '@':
    print('False')
else:
    print('True')
    howdy += 1


print('Valid password:', end=' ')
if howdy == 5:
    print('True')
else: 
    print('False')

