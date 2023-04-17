# #Write a function pay_bill which will take a list of expenses, percent commission, and a special offer amount
#
# If you don’t pass percent_comission it should be always 9.8%
#
# The Last argument special_offer_amount is not a required argument, you don’t need to pass it. Make it an optional parameter.
#
# If you want to give a special offer to the user, then you have to pass the third argument special_offer_amount. If the user makes the purchase greater than special_offer_amount, then give him an extra commission of 1.2%.
#
# Calculate the final payable price of the bill and return it from the function.
#

def pay_bill(expenses, percent_commision = 0.098, special_offer_amt = None):
    tot_expense =0
    for i, expense in enumerate(expenses):
        tot_expense += expense
    if special_offer_amt:
        if tot_expense >= special_offer_amt:
            percent_commision += 0.012
            print("Congratulations you have earned extra 1.2% extra comission")

    dis_amt = tot_expense * percent_commision
    final_amt = tot_expense - dis_amt

    return final_amt

bill = pay_bill([100,100,300])
print(bill)

bill = pay_bill([100, 145, 565, 322], 0.078)
print(bill)

print(pay_bill([200, 400, 86, 300, 500], 0.09, 800))

print(pay_bill([200, 400, 86, 300, 500], special_offer_amt=900))

print(pay_bill([200, 400, 86, 300, 500], percent_commision=0.1, special_offer_amt=1500))