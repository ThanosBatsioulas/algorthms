#!/usr/bin/env python

def fibonnaci(value):
    FibonnaciList = [1, 2]
    while FibonnaciList[len(FibonnaciList) - 1] < value:
        if (FibonnaciList[len(FibonnaciList) - 1] + FibonnaciList[len(FibonnaciList) - 2]) > value:
            break
        FibonnaciList.append(FibonnaciList[len(FibonnaciList) - 1] + FibonnaciList[len(FibonnaciList) - 2])

    return FibonnaciList

def even_Sum (list):
    sum = 0
    for element in list:
        if element % 2 == 0:
            sum = sum + element

    return sum


FibonnaciList = fibonnaci(4000000)
evenSum = even_Sum(FibonnaciList)

print "the sum of even-valued terms is", evenSum
