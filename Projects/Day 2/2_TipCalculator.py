print("Welcome to the tip calculator!")
bill = float(input("What was the total bill without tip? $"))
tip = int(input("What percentage tip would you like to give? 10%, 12% or 15%? "))
people = int(input("How many people to split the bill? "))
totalamount=(bill * (tip/100) + bill)
print(f"Total Bill: {totalamount}")
print(f"Each person will pay ${round(totalamount/people, 2)}")



