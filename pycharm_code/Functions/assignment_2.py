# Write a python function that will take n as input and print the pattern of n rows.
# If the n is even, then print it flipped.
# Example:
#
# n=3
# *
# * *
# * * *
#
# n=4
# * * * *
# * * *
# * *
# *

def even_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def odd_pattern(n):
    for i in range(1, n):
        for j in range(i):
            print("*", end=" ")
        print()

num = int(input("Enter Number: "))

if num % 2 == 0:
    even_pattern(num)
else:
    odd_pattern(num)

