# Write a Python program to find the sum of all the numbers except odd numbers between 1 and 20 using a loop.
# Can you also do this using a while loop?

n = 21
sum = 0
for i in range(0,n,2):
    #print(i,end=" ")
    if i%2 !=0:
        continue
    else:
        sum += i

print(f'Sum of numbers between 1 and 20 except odd numbers is: {sum}')