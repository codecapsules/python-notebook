warriors = ("Goku", "Vegeta")
warriors = warriors + ("Piccolo",)
bad_guys = [("Frieza", "Emperor"), ("Cell", "Android"), ("Buu", "Demon")]

print(warriors)  # ('Goku', 'Vegeta', 'Piccolo')
print(type(warriors))  # <class 'tuple'>

print(dict(bad_guys))  # {'Frieza': 'Emperor', 'Cell': 'Android', 'Buu': 'Demon'}
