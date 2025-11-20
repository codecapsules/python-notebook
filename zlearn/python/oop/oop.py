class Character(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.race = "Human"
        self.abilities = []

    def __str__(self):
        return f"{self.name} an {self.race}: {self.age} years old"

    def __len__(self):
        return len(self.abilities)

    @property
    def year_of_birth(self):
        return 2025 - int(self.age)


class Sayan(Character):
    planet = "VEGETA"

    def __init__(self, name, age, race, power):
        super().__init__(name, age)
        self.race = race
        self.power = power

    @classmethod
    def from_planet(cls):
        return f"Inhabitants of this class are from planet: {cls.planet}"


broly = Sayan("Broly", 30, "Sayan", 12.000)
broly.abilities.append("Mega-Canon")
broly.abilities.append("Planet-Eraser")

print(len(broly))
print(broly.year_of_birth)

print(Sayan.from_planet())
