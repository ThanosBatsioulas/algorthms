#!/usr/bin/env python

def multiplyList(list):
    return reduce(lambda x, y: x*y, list)

primeFactors = [1]
number = 600851475143
factor = 2

while multiplyList(primeFactors) < 600851475143:
    if number % factor == 0:
        number = number / factor
        primeFactors.append(factor)
    else:
        factor = factor + 1

print(primeFactors)
