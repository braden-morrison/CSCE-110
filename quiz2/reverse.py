num = input("enter plate number: ")
let = num[0:2]
num1 = num[2:9]
num1 = num1[::-1]
num2 = let + num1
print('reversed plate number:', num2)