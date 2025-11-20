warriors = [
    {"name": "Goku", "race": "Sayan", "planet": "Vegera"},
    {"name": "Vegeta", "race": "Sayan", "planet": "Vegeta"},
    {"name": "Broly", "race": "Sayan", "planet": "Vegeta"},
    {"name": "Piccolo", "race": "Namek", "planet": "Namek"},
]

for warrior in warriors:
    print(f"{warrior["name"].upper()} is a {warrior['race']} from {warrior['planet']}.")
