# Let's say you are doing push-ups and you have to complete 50 push-ups daily, write a program that,
#
# Upon completing 10 push-ups in a go, asks you, “Are you tired?”
#
# If you reply “yes” or “y” then it should break and print “You did total push-ups.”
#
# For example: If you did only 30  push-ups and answered “yes” to your program. It will break the loop and print “You did a total of 30 push-ups”
#
# If you reply “no” or “n” then it should continue and display how many push-ups are remaining  now after that ask you again “Are you tired?”
#
# For Example: if you answered “no” then it should display that 20 push-ups are remaining and ask you again “Are you tired?”
#
# If you complete all 50 push-ups, then it should print the “Congratulations! You made it” and stopped the program.


num_of_push_up = 10
repeation = 5 #total_set_of_push_up
total_push_up = repeation *  num_of_push_up
flag = False
for i in range(1, total_push_up):
    print("Doing pushup")
    if i % num_of_push_up == 0:
         n = input("Are you Tried?(yes/no).. ")
         if n == "y" or n == "yes":
             print(f'You did total push-ups. {i}')
             flag = True
             break
         elif  n == "n" or n == "no":
             remaining_push_up = total_push_up - i
             print(f'Remaining Push-ups are: {remaining_push_up}')
         else:
             prinf("Invalid input ...")
             flag = True
             break


if flag != True:
    print('Congratulations! You made it')