# After throwing the dice several times, you got this result,
#
# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# Using a for loop find out the followings:
# How many times have you got 6s
#
# How many times have you got 1s
#
# How many times have you got 6s two times in a row
#

dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]

result_1 = dice_result.count(6)
result_2 = dice_result.count(1)

print(f'You have got 6s in {result_1} times')
print(f'You have got 1s in {result_2} times')

l = len(dice_result)
count = 0
for i in range(l-1):
    if dice_result[i] == 6 and dice_result[i+1] == 6:
        count += 1

print(f'You have got 6s two times in row {count}')

