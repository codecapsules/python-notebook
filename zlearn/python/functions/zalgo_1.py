cars = [
    {"constructor": "Suzuki", "model": "Swift", "kilometers": 3000, "consumption": 5.2},
    {"constructor": "Hundai", "model": "i-20", "kilometers": 3000, "consumption": 5.1},
    {"constructor": "Toyota", "model": "Yaris", "kilometers": 3000, "consumption": 3.7},
    {
        "constructor": "Dacia",
        "model": "Sandero",
        "kilometers": 3000,
        "consumption": 3.9,
    },
]


def car_name(car):
    return f"{car['constructor']} {car['model']}"


def calculate_consumption(car):
    liters = car["kilometers"] * car["consumption"] / 100
    return liters


for car in cars:
    liters = calculate_consumption(car)
    name = car_name(car)

    print(f"{name} consumed {liters} liters")
