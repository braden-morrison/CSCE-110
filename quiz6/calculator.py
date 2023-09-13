a = int(input("Enter a: "))
b = int(input("Enter b: "))
a_B = bin(a)
b_B = bin(b)
notA = bin(~a)
A_and_B = bin(a & b)
a_or_b = bin(a | b)
a_xor_b = bin(a ^ b)
a_xor_b = int(a_xor_b, 2) << 3
a_xor_b = bin(a_xor_b)
# a_xor_b = int(a_xor_b) << 3
print(a, 'in binary:', a_B)
print(b, 'in binary:', b_B)
print('(NOT ', a, ') in binary: ', notA, sep='')
print('(', a, ' AND ', b, ') in binary: ', A_and_B, sep='')
print('(', a, ' OR ', b, ') in binary (without prefix): ', a_or_b[2:], sep='')
print('(', a, ' XOR ', b, ') shifted left by 3 positions in binary: ',
      a_xor_b, sep='')
