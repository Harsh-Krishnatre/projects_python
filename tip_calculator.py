#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill_total = input("What was the total bill? $")
bill_total = float(bill_total)
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_percentage = int(tip_percentage)
people_number = int(input("How many people to split the bill? "))
pay_per_person = (bill_total + (tip_percentage * bill_total/100))/people_number
pay_per_person = round(pay_per_person,2)
print(f"Each person should pay: ${pay_per_person}")
