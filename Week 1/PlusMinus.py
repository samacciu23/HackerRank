'''
DESCRIPTION:
Given an array of integers, calculate the ratios of its elements
that are positive, negative, and zero. Print the decimal value of each fraction
on a new line with 6 places after the decimal.

SAMPLE INPUT:
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

SAMPLE OUTPUT:
0.500000
0.333333
0.166667

EXPLANATION:
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are
positive: 3/6 = 0.500000,
negative:  2/6 = 0.333333
and zeros: 1/6 = 0.166667.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_zero = 0
    count_pos = 0
    count_neg = 0
    for i in arr:
        if i == 0:
            count_zero+=1
        if i > 0:
            count_pos+=1
        if i < 0:
            count_neg+=1
    print(count_pos/len(arr))
    print(count_neg/len(arr))
    print(count_zero/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)




