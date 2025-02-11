# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = tip / 100 * bill    #Total tip percent
total_bill = total_tip + bill       #Total bill after adding the tip
bill_per_person = total_bill / people       #Bill to be split by total person

print(f"Each person should pay: ${round(bill_per_person, 2)}")