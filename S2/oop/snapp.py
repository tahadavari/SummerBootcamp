class Driver:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, driver: Driver):
        self.driver: Driver = driver


class Trip:
    def __init__(self, src, dst, car: Car):
        self.car: Car = car
        self.src = src
        self.dst = dst


mamad = Driver('mamd')

car_mamd = Car(mamad)

trip1 = Trip("Nazar", "Mosala", car_mamd)
print(trip1.car.driver.name)
