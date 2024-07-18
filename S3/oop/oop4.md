<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: 'Vazirmatn', sans-serif;
            direction: rtl;
            text-align: right;
        }
        pre {
            background-color: #2276bb;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
    <link href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@latest/dist/font-face.css" rel="stylesheet" type="text/css" />
    <title>اصول چهارگانه شی‌گرایی در پایتون</title>
</head>
<body>

<h1>اصول چهارگانه شی‌گرایی در پایتون</h1>

<h2>کپسوله‌سازی (Encapsulation)</h2>
<p>
کپسوله‌سازی به مخفی‌سازی جزئیات داخلی یک شی و ارائه یک رابط عمومی به کاربر اشاره دارد. این اصل با استفاده از متدها و متغیرهای خصوصی و عمومی پیاده‌سازی می‌شود.
</p>
<h3>مثال در پایتون</h3>
<pre>
<code>
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Insufficient balance')
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)  # Output: Insufficient balance
</code>
</pre>

<h2>وراثت (Inheritance)</h2>
<p>
وراثت به مفهوم استفاده مجدد از کد از طریق ایجاد کلاس‌های جدید از کلاس‌های موجود اشاره دارد. این اصل امکان گسترش و تغییر رفتار کلاس‌ها را فراهم می‌کند.
</p>
<h3>مثال در پایتون</h3>
<pre>
<code>
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meow!'

fido = Dog('Fido')
tom = Cat('Tom')
print(fido.speak())  # Output: Fido says Woof!
print(tom.speak())   # Output: Tom says Meow!
</code>
</pre>

<h2>چندریختی (Polymorphism)</h2>
<p>
چندریختی به قابلیت استفاده از یک رابط واحد برای انواع مختلف اشیا اشاره دارد. این اصل به تعریف متدهایی با نام یکسان در کلاس‌های مختلف می‌پردازد که رفتار متفاوتی دارند.
</p>
<h3>مثال در پایتون</h3>
<pre>
<code>
class Bird:
    def fly(self):
        return 'Flying high!'

class Penguin(Bird):
    def fly(self):
        return 'I can\'t fly, but I can swim!'

# Example of polymorphism
def describe_flight(bird):
    return bird.fly()

sparrow = Bird()
penguin = Penguin()
print(describe_flight(sparrow))  # Output: Flying high!
print(describe_flight(penguin))  # Output: I can't fly, but I can swim!
</code>
</pre>

<h2>انتزاع (Abstraction)</h2>
<p>
انتزاع به فرایند ساده‌سازی سیستم‌های پیچیده با مخفی کردن جزئیات غیرضروری و ارائه جزئیات مهم اشاره دارد. این اصل با تعریف کلاس‌ها و متدهای انتزاعی پیاده‌سازی می‌شود.
</p>
<h3>مثال در پایتون</h3>
<pre>
<code>
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

# Example of abstraction
shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())  # Output: 12, 78.5
</code>
</pre>

</body>
</html>