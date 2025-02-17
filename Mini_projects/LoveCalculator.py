# Love Calculator

print("The Love Calculator is calculating your score...")

name1 = input("Enter your name: ").lower()
name2 = input("Enter his/her name: ").lower()

combined_names = name1 + name2
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you are like coke and mentos.")
elif (love_score > 40) or (love_score < 50):
    print(f"Your love score is {love_score}, you are already together.")
else:
    print(f"Your love score is {love_score}")