#You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.Please use list comprehensions rather than multiple loops
x = int(input("Write the x co-ordinates\n"))
y = int(input("Write the y co-ordinates\n"))
z = int(input("Write the z co-ordinates\n"))
n = int(input("Write the n co-ordinates\n"))
x_coordinates = [a for a in range(x+1)]
y_coordinates = [a for a in range(y+1)]
z_coordinates = [a for a in range(z+1)]
ListOfCoordinates = [[p,q,r] for p in x_coordinates for q in y_coordinates for r in z_coordinates if p+q+r!=n]
print(ListOfCoordinates)