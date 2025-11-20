# warriors = list("Goku", "Vegeta", "Piccolo", "Gohan")
warriors = ["Goku", "Vegeta", "Piccolo", "Gohan"]
characters = [
    ["Goku", "Vegeta"],
    ["Vegeta", "Vegeta"],
    ["Gohan", "Earth"],
    ["Trunks", "Earth"],
]

warriors.append("Krilin")  # ["Goku", "Vegeta", "Piccolo", "Gohan", "Krilin"]
warriors.remove("Krilin")  # ["Goku", "Vegeta", "Piccolo", "Gohan"]
characters.append(["Krilin", "Earth"])
characters.remove(["Krilin", "Earth"])

print(type(warriors))  # <class 'list'>
print(warriors[0])  # Goku
print(warriors[1])  # Vegeta
print(warriors[-1])  # Gohan

print(len(warriors))  # 4
print(characters[0][0])  # Goku

bads = ["Freeza", "Cell", "Buu"]

all_characters = warriors + bads
all_characters.insert(0, "Broly")

print(
    all_characters
)  # ['Broly', 'Goku', 'Vegeta', 'Piccolo', 'Gohan', 'Freeza', 'Cell']

print(all_characters.index("Vegeta"))  # 0

first = all_characters.pop(0)
last = all_characters.pop()
print(first)  # Broly
print(last)  # Buu

print(all_characters[:2])  # ['Goku', 'Vegeta']
print(all_characters[2:])  # ['Piccolo', 'Gohan', 'Freeza', 'Cell']
print(all_characters[1:3])  # ['Vegeta', 'Piccolo']
