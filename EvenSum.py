number = input("Enter numbers: ").split()
even_sum = 0

for num in number:
    num = int(num)
    if num % 2 == 0:
        even_sum += num
        
print(f"Sum of even numbers: {even_sum}")