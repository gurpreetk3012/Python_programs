## BMI calculator

height = float(input("Enter the height (in meters): "))
weight = float(input("Enter the weight (in kilograms): "))

Bmi = weight / (height * height)

if Bmi < 18.5:
    print(f"Your Bmi is {Bmi}, You are underweight.")
elif 18.5 < Bmi < 25:
    print(f"Your Bmi is {Bmi}, You have a normal weight.")
elif 25 < Bmi < 30:
    print(f"Your Bmi is {Bmi}, You are slightly overweight.")
elif 30 < Bmi < 35:
    print(f"Your Bmi is {Bmi}, You are obese.")
else:
    print(f"Your Bmi is {Bmi}, You are clinically obese.")