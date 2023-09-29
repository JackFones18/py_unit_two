amount = input("Enter an amount in dollars and cents (ex. 123.12): ")
decimal_amount = float(amount)

r_hundreds = round(decimal_amount % 100, 2)
hundreds = round((decimal_amount - r_hundreds) / 100)

r_fifty = round(r_hundreds % 50, 2)
fifties = round((r_hundreds - r_fifty) / 50)

r_twenties = round(r_fifty % 20, 2)
twenties = round((r_fifty - r_twenties) / 20)

r_tens = round(r_twenties % 10, 2)
tens = round((r_twenties - r_tens) / 10)

r_fives = round(r_tens % 5, 2)
fives = round((r_tens - r_fives) / 5)

r_ones = round(r_fives % 1, 2)
ones = round((r_fives - r_ones) / 1)

r_quarters = round(r_ones % .25, 2)
quarters = round((r_ones - r_quarters) / .25)

r_dimes = round(r_quarters % .1, 2)
dimes = round((r_quarters - r_dimes) / .1)

r_nickels = round(r_dimes % .05, 2)
nickels = round((r_dimes - r_nickels) / .05)

r_pennies = round(r_nickels % .01, 2)
pennies = round((r_nickels - r_pennies) / .01)

print("you will need:")

#learned if statements from https://www.w3schools.com/python/python_conditions.asp
if hundreds > 0:
    print(hundreds, "hundred dollar bill(s)")
if fifties > 0:
    print(fifties, "fifty dollar bill(s)")
if twenties > 0:
    print(twenties, "twenty dollar bill(s)")
if tens > 0:
    print(tens, "ten dollar bill(s)")
if fives > 0:
    print(fives, "five dollar bill(s)")
if ones > 0:
    print(ones, "one dollar bill(s)")
if quarters > 0:
    print(quarters, "quarters")
if dimes > 0:
    print(dimes, "dimes")
if nickels > 0:
    print(nickels, "nickels")
if pennies > 0:
    print("and", pennies, "pennies")
