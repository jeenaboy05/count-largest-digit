
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countLargestDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER base
#  3. INTEGER start
# 
#
#
# Author: Aryan Jeena
# Date: 1/14/23

#Generate numbers in base 10 and count up "num" numbers
def generateNumbers(num, base, start):
    numbers = [convertToBase10(start,base)]
    while len(numbers) < num:
        current = numbers[-1] + 1
        digits = []
        while current:
            digits.append(current % base)
            current //= base
        digits.reverse()
        numbers.append(int(''.join(map(str, digits)), base))
    return numbers

#Convert to base "base"
def convertToBase(num, base):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return int(''.join(map(str, digits[::-1])))

#Convert to base 10
def convertToBase10(num, base):
    base10Num = 0
    num = str(num)[::-1]
    for i in range(len(num)):
        base10Num += int(num[i]) * (base ** i)
    return base10Num
    
#Count amount of times largest digit appears in base "base" and return amount in base 10.
def countLargestDigit(num, base, start):
    numbers = generateNumbers(num, base, start)
    largestDigit = str(base - 1)
    count = 0
    for number in numbers:
        numberAfterConvert = convertToBase(number, base)
        count += str(numberAfterConvert).count(largestDigit)
    print(count)


usernum = input("What is the number you want to count: ")
userbase = input("What base would you want to convert to: ")
userstart = input("What number would you like to start with: ")
countLargestDigit(int(usernum), int(userbase), int(userstart))