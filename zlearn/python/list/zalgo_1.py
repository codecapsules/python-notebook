warriors_deck = ["Goku", "Vegeta", "Piccolo", "Gohan"]

user_input = input("Enter a name: ").lower()

if user_input in [warrior.lower() for warrior in warriors_deck]:
    print(f"{user_input.capitalize()} is in the deck")
else:
    print(f"{user_input} is NOT in the deck")
