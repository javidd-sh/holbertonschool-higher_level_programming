#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # Bu kod değiştirilmeyecek

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
