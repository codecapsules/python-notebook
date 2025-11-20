lost_numbers = [4, 8, 15, 16, 23, 42]
odds = [n for n in lost_numbers if n % 2 != 0]
evens = [n for n in lost_numbers if n % 2 == 0]

print(odds)  # [15, 23]

################################################

warriors_deck = [
    "Goku",
    "Vegeta",
    "Piccolo",
    "Gohan",
    "Trunks",
    "Krilin",
    "Broly",
    "Yamcha",
]
sayans_portal = ["Goku", "Vegeta", "Gohan", "Trunks", "Broly"]

in_portal = [warrior for warrior in warriors_deck if warrior in sayans_portal]

print(in_portal)  # ['Goku', 'Vegeta', 'Gohan', 'Trunks', 'Broly']
