class Test:

    def __init__(self, name):
        self.name = name 

    # def __add__(self, other):
    def __str__(self):
        return self.name


# test_obj = Test("Name")
# test_int = 123 

# test_1 = 12 + 12

# print(test_obj) #<__main__.Test object at 0x0000025B04BA86E0>

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         print(self.x)
#         print(other.x)
    
#     def __lt__

# obj_1 = Vector(12, 13)
# obj_2 = Vector(22, 23)

# test_2 = obj_1 + obj_2

# class Money:
#     def __init__(self, currency, sum):
#         self.currency = currency
#         self.sum = sum 
    
#     def convert_to_coin(self, obj):
#         pass

#     def __add__(self, other):
#         # if self.currency != "coin" and self.currency != "coin":
#         #     self.convert_to_coin(self)
#         #     self.convert_to_coin(other) 
#         if self.currency != other.currency:
#             pass

# kg = Money("SOM", 100)
# us = Money("USD", 100)

# homyak.coin = kg + us
"""
🎯 Цель

Закрепить работу с магическими методами:

__add__

__sub__

__mul__

__truediv__

и научиться работать с логикой внутри класса.

 

📌 Задание

Создайте класс Money.

 

🔹 Атрибуты класса

В конструкторе должны быть два атрибута:

amount — сумма денег

currency — валюта

Пример:

 

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

 

🔹 Курсы валют

В начале файла создайте словарь курсов валют относительно сома.

Пример:

 

rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

 

Где:

ключ — валюта

значение — сколько сомов стоит 1 единица валюты

 

🔹 Метод конвертации

В классе должен быть метод:

convert_to_kgs()

 

Этот метод должен переводить любую валюту в сомы.

Пример:

100 USD → 8900 KGS

 

🔹 Магические методы

Реализуйте следующие магические методы:

__add__

Сложение денег.

money1 + money2

 

Если валюты разные, сначала нужно конвертировать их в сомы, затем выполнить сложение.

__sub__

Вычитание денег.

money1 - money2

 

Также нужно учитывать конвертацию валют.

__mul__

Умножение денег на число.

Пример:

money * 3

 

__truediv__

Деление денег на число.

Пример:

money / 2

 

🔹 Метод __str__

Чтобы объект красиво выводился.

Пример:

 

print(money)

 

Вывод:

100 USD

 

📌 Пример использования

 

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result = money1 + money2

print(result)
"""


rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def convert_to_kgs(self):
        if self.currency not in rates:
            raise ValueError(f"Неизвестная валюта: {self.currency}")
        return self.amount * rates[self.currency]
    
    def convert_from_kgs(self, amount_in_kgs, target_currency):
        if target_currency not in rates:
            raise ValueError(f"Неизвестная валюта: {target_currency}")
        return amount_in_kgs / rates[target_currency]
    
    def to_currency(self, target_currency):
        kgs_amount = self.convert_to_kgs()
        new_amount = kgs_amount / rates[target_currency]
        return Money(new_amount, target_currency)
    
    def __add__(self, other):
        if isinstance(other, Money):
            kgs1 = self.convert_to_kgs()
            kgs2 = other.convert_to_kgs()
            
            total_kgs = kgs1 + kgs2
            
            result_amount = total_kgs / rates[self.currency]
            return Money(result_amount, self.currency)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Money):
            kgs1 = self.convert_to_kgs()
            kgs2 = other.convert_to_kgs()
            
            total_kgs = kgs1 - kgs2
            
            result_amount = total_kgs / rates[self.currency]
            return Money(result_amount, self.currency)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            return Money(self.amount / other, self.currency)
        return NotImplemented
    
    def __str__(self):
        if self.amount == int(self.amount):
            amount_str = str(int(self.amount))
        else:
            amount_str = f"{self.amount:.2f}"
        return f"{amount_str} {self.currency}"
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    


money1 = Money(100, "USD")
money2 = Money(5000, "KGS")
money3 = Money(50, "EUR")
money4 = Money(1000, "RUB") 
    

print(f"money1 = {money1}")
print(f"money2 = {money2}")
print(f"money3 = {money3}")
print(f"money4 = {money4}")

print(f"{money1} = {money1.convert_to_kgs()} KGS")
print(f"{money3} = {money3.convert_to_kgs()} KGS")
print(f"{money4} = {money4.convert_to_kgs()} KGS")

result1 = money1 + money2
print(f"{money1} + {money2} = {result1}")

result2 = money3 + money4
print(f"{money3} + {money4} = {result2}")

result3 = money2 - money1
print(f"{money2} - {money1} = {result3}")

result4 = money3 - money4
print(f"{money3} - {money4} = {result4}")

result5 = money1 * 3
print(f"{money1} * 3 = {result5}")

result6 = 2 * money2 
print(f"2 * {money2} = {result6}")

result7 = money2 / 2
print(f"{money2} / 2 = {result7}")

result8 = money3 / 4
print(f"{money3} / 4 = {result8}")

print(f"{money1}")
print(f"{money2}")
print(f"{money3}")
print(f"{money4}")

print(f"{money1} == {money2}? {money1 == money2}")

converted = money1.to_currency("EUR")
print(f"{money1} в EUR = {converted}")

money_a = Money(100, "USD")
money_b = Money(5000, "KGS")
result = money_a + money_b
print(f"{money_a} + {money_b} = {result}")