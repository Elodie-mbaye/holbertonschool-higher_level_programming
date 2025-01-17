#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Last_digit = -(-number % 10)
else:
    Last_digit = number % 10
print(f"Last_digit of {number} is {Last_digit}", end = " ")
if Last_digit > 5:
    print(f"{Last_digit} and is greater than 5")
elif str == 0:
    print(f"{Last_digit} and is 0")
else:
    print(f"{Last_digit} and is less than 6 and not 0")
