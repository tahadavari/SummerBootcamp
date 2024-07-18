class Bird:
    def fly(self):
        return "Flying"


class Duck(Bird):
    pass


class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")


def let_bird_fly(bird):
    return bird.fly()


duck = Duck()
ostrich = Ostrich()

print(let_bird_fly(duck))
print(let_bird_fly(ostrich))
