# File: extra_credit.py
# Author: Braden Morrison
# Date: 06/10/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: asks for pos num, then recursively adds the sum from 1 up to a number


def calculate_sum(n):
    if n < 1:
        return 0
    
    return n + calculate_sum(n - 1)


n = int(input("Enter a number: "))
print()
total_sum = calculate_sum(n)
print(f"The sum from 1 to {n} is {total_sum}")

