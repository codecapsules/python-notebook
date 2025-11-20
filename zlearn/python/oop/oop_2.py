class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __repr__(self):
        return f"<Garage : {self.cars}>"

    def add(self, car):
        self.cars.append(car)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(
                f"Tried to add a non Car object: {car.__class__.__name__} to garage"
            )
        self.cars.append(car)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car : {self.make} {self.model}>"


garage = Garage()
fiesta = Car("Ford", "Fiesta")
mustang = Car("Ford", "Mustang")


def add_car(classed, car):
    try:
        classed.add_car(car)
    except TypeError:
        print("TypeError: Your car is not a car.")
    finally:
        print(f"The Garage now has {len(classed)} cars.")


add_car(garage, "fiesta")
