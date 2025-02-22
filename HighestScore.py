students_scores = input("Enter students score: ").split()
num_students = len(students_scores)

for n in range(0, num_students):
    students_scores[n] = int(students_scores[n])

highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class: {highest_score}")