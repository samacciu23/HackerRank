'''
DESCRIPTION:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
SAMPLE INPUT:
3
11 2 4
4 5 6
10 8 -12
SAMPE OUTPUT:
15
'''
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    d1, counter1 = 0, 0
    d2, counter2 = 0, len(arr) - 1
    for row in arr:
        d1 += row[counter1]
        d2 += row[counter2]
        counter1 += 1
        counter2 -= 1
    return abs(d1 - d2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
