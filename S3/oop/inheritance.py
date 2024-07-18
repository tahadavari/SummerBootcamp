class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"i am animal {self.name}"


class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof!'


class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meow!'


fido = Dog('Fido')
tom = Cat('Tom')
print(fido.speak())
print(tom.speak())
