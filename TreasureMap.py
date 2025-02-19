print("Hiding your treasure ? 'X' mark to the place.")

line_1 = ['■', '■', '■']
line_2 = ['■', '■', '■']
line_3 = ['■', '■', '■']
map = [line_1, line_2, line_3]

position = input("Give the position like rows are in alphabets from A and columns are in numbers from 1(B2,C1....)\n")
alphabet = position[0].lower()
abc = ['a', 'b', 'c']
row_index = abc.index(alphabet)
column_index = int(position[1]) - 1

map[row_index][column_index] = 'X'
print(f"{line_1}\n{line_2}\n{line_3}")