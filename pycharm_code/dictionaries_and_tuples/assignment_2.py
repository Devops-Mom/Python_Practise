# You and your wife argued about expenses last night.
# You both want to know who is spending more in a month.
# Now you both go to the Little Yoda he is a good python programmer.
# He suggested that both of you add an entry in a dictionary next time you spend money.
# So that you can have a clear picture of your expenses and plan to reduce them.
# Both dictionaries are as below-
#
# Your expenses -
# Clothes - 1100
# Shoes - 1000
# Watch - 900
# Mobile Recharge - 699
# Petrol - 1980
#
# Your Wife’s expenses -
# Mobile Recharge - 799
# DTH recharge - 999
# Clothes - 2310
# Makeup - 3670
# Shoes - 999
#
# Find out the total expenses for each of you.
# Find out who spending more
# Find out which thing you and your wife spending more

expenses = {
    'husband' : {
         'clothes' : 1100,
         'shoes' : 1000,
         'watch' : 900,
         'mob_recharge' : 699,
         'petrol' : 1980
    },
    'wife' : {
        'mob_recharge' : 799,
        'DTH recharge' : 999,
        'clothes' : 2310,
        'makeup' : 3670,
        'shoes' : 999
    }
}

# Find out the total expenses for each of you.

total_expense = []
for person,expense in expenses.items():
    #print(f'{person} --- {expense}')
    total = 0
    for i,amt in expense.items():
        #print(f'{i} --- {amt}')
         total += amt
    total_expense.append(total)

print(f"Husband expenses: {total_expense[0]}")
print(f"Wife expenses: {total_expense[1]}")

# Find out who spending more
if total_expense[0] < total_expense[1]:
    print(f"Husband's expenses is less than Wife's expense")
else:
    print(f"Wife's expenses is less than Husband's expense")

# Find out which thing you and your wife spending more

flag = 'H'
for j, expense in expenses.items():
    expensive = 0
    item = ""
    for i, amt in expense.items():
        if expensive < amt:
            expensive = amt
            item = i

    if flag == 'H':
       print(f"Husband's spend more on {item} -- {expensive} Rs ")
       flag = 'W'   # Wife's Turn
    else:
       print(f"Wife's spend more on {item} -- {expensive} Rs ")

