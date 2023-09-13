# File: barcode.py
# Author: Braden Morrison
# Date: 07/06/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: 

def get_rc(rows, cols, letter):
    matrix = []
    y = 0
    for y in range(rows):
        successful = False
        while not successful:
            list = []
            list = [int(x) for x in input("Matrix {} row {}: ".format(letter, (y+1))).split()]
            if len(list) == int(cols):
                successful = True
                matrix.append(list)
    return matrix

def print_matrix(matrix, rows, letter):
    print('Matrix ', letter, ':', sep= '')
    for x in matrix:
        for y in range(len(x)):
            print(f"{x[y] : <5}", end= " ")
        print()

def matrix_C(A, rows, cols2, B, cols):
    matrixC1 = []
    for z in range(rows):
        matrixC1.append([])
        for y in range(cols):
            val = 0
            for x in range(cols2):
                val += A[z][x] * B[x][y]
            matrixC1[z].append(val)
    return matrixC1


def matrix_T(C, rows, cols):
    matrix = []
    for x in range(cols):
        matrix.append([])
        for y in range(rows):
            matrix[x].append(C[y][x])
    return matrix
            


def barcode(C, rows, cols):
    code = '|'
    for x in range(cols):
        val = 0
        for y in range(rows):
            val += C[y][x]
        code += str(val) + '|'
    return code

            

    

ar, ac = input("Matrix A number of rows and columns: ").split()
if (int(ar) > 10 or int(ac) > 10):
     ar, ac = input("Matrix A number of rows and columns: ").split()
br, bc = input("Matrix B number of rows and columns: ").split()
if (int(br) > 10 or int(bc) > 10):
    br, bc = input("Matrix B number of rows and columns: ").split()


if int(ac) != int(br):
    print("Matrix A: (", ar, "x", ac, ") Matrix B: (", br, "x", bc, ") cannot be multiplied.", sep= "")
else:
    print()
    matrixA = get_rc(int(ar), ac, 'A')
    print()
    matrixB = get_rc(int(br), bc, 'B')
    print()

    print_matrix(matrixA, int(ar), 'A')
    print()
    print_matrix(matrixB, int(br), 'B')
    print()
    
    matrixC = matrix_C(matrixA, int(ar), int(ac), matrixB, int(bc))
    print_matrix(matrixC, int(ar), 'C')
    print()

    matrixT = matrix_T(matrixC, int(ar), int(bc))
    print_matrix(matrixT, int(bc), 'T')
    print()

    barcode1 = barcode(matrixC, int(ar), int(bc))
    print('Barcode: ')
    print(barcode1)









