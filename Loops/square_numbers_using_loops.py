#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n, print i2.
n = int(input("Enter the number\n"))
i = 0
print("The square of all non-negative number is")
while i != n:
    print(i*i)
    i += 1