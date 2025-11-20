def divide(x, y):
    return x / y


divide = lambda x, y: x / y

print(divide(10, 2))  # 5.0
print((lambda x, y: x / y)(10, 2))  # 5.0

average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Alice", "grades": [5, 4, 4, 5]},
    {"name": "Bob", "grades": [3, 4, 4, 2]},
    {"name": "Cathy", "grades": [5, 5, 5, 4]},
]

for student in students:
    print(f"{student['name']} has an average grade of {average(student['grades'])}")
