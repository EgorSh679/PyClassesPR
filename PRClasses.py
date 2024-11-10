class Soda:
    def __init__(self, add_on=None):
        self.add_on = add_on

    def show_my_drink(self):
        if self.add_on:
            print(f"Газировка и {self.add_on}")
        else:
            print("Обычная газировка")

class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_triangle(self):
        a, b, c = self.sides
        
        if not all(isinstance(x, int) for x in self.sides):
            print("Нужно вводить только числа!")
        
        if any(x <= 0 for x in self.sides):
            print("С отрицательными числами ничего не выйдет!")
        
        if a + b > c and a + c > b and b + c > a:
            print("Ура, можно построить треугольник!") 
        else:
            print("Жаль, но из этого треугольник не сделать.")

class KgToPounds:
    def __init__(self, kg):
        self._kg = kg 

    def to_pounds(self):
        return self._kg * 2.20462 #кг в фунты

    @property
    def kg(self):
        return self._kg #геттер возвращения циферки кг
        
    @kg.setter
    def kg(self, value): #сеттер для нового значения кг 
        if value < 0:
            raise ValueError("Количество килограммов не может быть отрицательным!")
        self._kg = value

class Nikola:
    def __init__(self, name, age):
        if name.lower() == "николай":
            self._name = name
        else:
            self._name = "Я не {name}, а Николай"

        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __setattr__(self, key, value):
        if key in ['_name', '_age']:
            super().__setattr__(key, value)
        else:
            raise AttributeError("Нельзя добавлять новые атрибуты к экземпляру Nikola")

class RealString:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.value) == len(other.value)
        elif isinstance(other, str):
            return len(self.value) == len(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.value) < len(other.value)
        elif isinstance(other, str):
            return len(self.value) < len(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RealString):
            return len(self.value) > len(other.value)
        elif isinstance(other, str):
            return len(self.value) > len(other)
        return NotImplemented

class Transaction:
    def __init__(self, amount, date, currency='USD', usd_conversion_rate=1, description=None):
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = usd_conversion_rate
        self._description = description

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency

    @property
    def usd_conversion_rate(self):
        return self._usd_conversion_rate

    @property
    def description(self):
        return self._description
    
    @property
    def usd(self):
        return self._amount * self._usd_conversion_rate


Name1 = Soda("чай")
Name1.show_my_drink()

Name2 = TriangleChecker(4, 2, 3)
Name2.is_triangle()

Name3 = KgToPounds(3)
print(Name3.kg)
print(Name3.to_pounds())
Name3.kg = 30
print(Name3.kg)

Name4 = Nikola("Николай", 30)
print(Name4.name)
print(Name4.age)
try:
    Name4.petr = "Петр"
except AttributeError as e:
    print(e)

a = RealString("Apple")
b = RealString("Яблоко")
print(a < b)
print(a == "Orange")

trans = Transaction(100, "2023-10-02", "EUR", 1.1, "Payment for services")
print(trans.amount)
print(trans.date)
print(trans.currency)
print(trans.usd_conversion_rate)
print(trans.description)
print(trans.usd)