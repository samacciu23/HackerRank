'''
DESCRIPTION:
Given five positive integers, find the minimum and maximum values
that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

SAMPLE INPUT:
1 2 3 4 5
SAMPLE OUTPUT:
10 14
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr = sorted(arr)
    min = sum(arr[:-1])
    max = sum(arr[1:])
    print(f'{min} {max}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
