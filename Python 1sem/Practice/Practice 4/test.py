from calculator.basic import add, subtract
from calculator.advanced import power, square_root
from calculator.basic import multiply
from calculator.advanced.trigonometry import *

import sys

print(sys.path)

print(sin(0))                # Вывод : 1.0
print(cos(0))                # Вывод : 0.0
print(tg(0))                 # Вывод : 1.0
print(multiply(4, 5))        # Вывод: 20
print(add(2, 3))             # Вывод: 5
print(subtract(5, 2))        # Вывод: 3
print(power(2, 3))           # Вывод: 8
print(square_root(16))       # Вывод: 4.0
