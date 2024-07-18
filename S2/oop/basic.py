class Car:
    count = 0

    def __init__(self, color, model, plate, x=0, y=0):
        self.color = color
        self.model = model
        self.plate = plate
        self.x = x
        self.y = y
        Car.count += 1

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y


car1 = Car("red", "samand", "23س۱۳۴")
car1.move(4, 45)


car2 = Car("asxas", "asxas", "asx23س۱۳۴")

print(car1.x, car1.y)
