numbers = [4, 8, 15, 16, 23, 42]

double_numbers = [n * 2 for n in numbers]
squared_numbers = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

print(double_numbers)  # [8, 16, 30, 32, 46, 84]

numbers_strings = [f"Lost numbers are: {n} " for n in numbers]
print(numbers_strings)  # ['Lost numbers are: 4', 'Lost numbers are: 8' ....]

################################################################################

warriors = ["Goku", "Vegeta", "Piccolo", "Gohan"]
lowers = [warrior.lower() for warrior in warriors]

print(lowers)  # ['goku', 'vegeta', 'piccolo', 'gohan']
