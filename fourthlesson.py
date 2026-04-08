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

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __add__(self, other):
    #     print(self.x)
    #     print(other.x)
    
    # def __lt__

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
