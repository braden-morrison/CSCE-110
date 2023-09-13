 

password = str(input("Enter a password: "))
print('No two consecutive identical characters:', end=' ')
valid3 = False
x = 0
for letter in password:
    if x + 1 == len(password):
        print('True')
        break
    if password[x] == password[x+1]:
        print('False')
        break
    x += 1
       
