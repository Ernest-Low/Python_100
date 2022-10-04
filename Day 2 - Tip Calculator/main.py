
# Day 2 Exercise
# Create a Tip Calculator

print("Welcome to the tip calculator.")
bill = input("What is the initial bill?: ")
tip_p = input("What percentage of tip would you like to give? 10/12/15 : ")
people = input("How many people are splitting the bill?: ")

final_bill = round(((float(bill) * ((100 + float(tip_p))/100) ) / float(people), 2)

print(f"Each person should pay: ${final_bill}")