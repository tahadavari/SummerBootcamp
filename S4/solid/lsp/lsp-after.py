from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    def move(self):
        return "Flying"


class NonFlyingBird(Bird):
    def move(self):
        return "Running"


class Duck(FlyingBird):
    pass


class Ostrich(NonFlyingBird):
    pass


def let_bird_move(bird):
    return bird.move()


duck = Duck()
ostrich = Ostrich()

print(let_bird_move(duck))
print(let_bird_move(ostrich))
