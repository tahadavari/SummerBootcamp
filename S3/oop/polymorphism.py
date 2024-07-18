class Bird:
    def fly(self):
        return 'Flying high!'


class Penguin(Bird):
    def fly(self):
        return 'I can\'t fly, but I can swim!'


def describe_flight(bird):
    return bird.fly()


sparrow = Bird()
penguin = Penguin()
print(describe_flight(sparrow))
print(describe_flight(penguin))
