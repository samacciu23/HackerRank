'''
DESCRIPTION:
Given an array of integers, where all elements but one occur twice, find the unique element.
SAMPLE INPUT:
array = [1,2,3,4,3,2,1]
SAMPLE OUTPUT:
4
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    while a[0] in a[1:]:
        m = a.pop(0)
        a.pop(a.index(m))
    for n in a:
        return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
