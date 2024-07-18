class Animal:  # Parent Class
    def __init__(self, age, voice):
        self.age = age
        self.voice = voice

    def animal_voice(self):
        print(self.voice)

    def speak(self):
        print("I am a animal")


class Cat(Animal):
    pass


class Dog(Animal):
    def speak(self):
        print("I am dog ")


cat = Cat(10, "mewww")
print(cat.age)
cat.animal_voice()
cat.speak()
dog = Dog(20, "hoooop")
dog.speak()
