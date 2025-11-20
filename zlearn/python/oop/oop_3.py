class Car(object):
    def __init__(self, id, manufac, model, color="white"):
        self.id = id
        self.manufac = manufac
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.id} - {self.manufac} {self.model}: {self.color}"

    def change_id(self, newid):
        self.id = newid


class Suv(Car):
    def __init__(self, id, manufac, model):
        super(Suv, self).__init__(self, id, manufac, model)


first = Suv(1, "Audi", "Q5")
print(first.color)
