# Write a python function to check if any given number is a prime number and odd number?
#

def prime_or_not(n):
    for i in range(2, n):
        if n % i == 0:
            return f'{n} Number is not Prime Number'

    return f'{n} Number is Prime Number'

n = int(input("Enter any number of your choice..: "))

result = prime_or_not(n)
print(result)
