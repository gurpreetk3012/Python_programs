#The included code stub will read an integer, n, from STDIN.
#Without using any string methods, try to print the following: 12...n
#Note that "..." represents the consecutive values in between.
print("Give the input\n")
n = int(input())
for i in range(1,n+1):
    print(str(i),end="")