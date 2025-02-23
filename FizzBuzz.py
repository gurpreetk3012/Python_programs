# FizzBuzz program: Prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.

target = 100

for num in range(1, target+1):

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)