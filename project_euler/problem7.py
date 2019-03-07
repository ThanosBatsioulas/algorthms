#!/usr/bin/env python
import math

def isPrimary(number):
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False

    return True


number = 2
i = 1
while i <= 10001:
    if isPrimary(number):
        primeNumber = number
        i = i + 1
    number = number + 1

print(primeNumber)
