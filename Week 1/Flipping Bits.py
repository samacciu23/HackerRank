'''
DESCRIPTION:
You will be given a list of 32 bit unsigned integers.
Flip all the bits ( and ) and return the result as an unsigned integer.
SAMPLE INPUT:
3
2147483647
1
0
SAMPLE OUTPUT:
2147483648
4294967294
4294967295
'''
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    bina = str(bin(int(n)))[2:]
    while len(bina) < 32:
        bina = '0' + bina
    flip = str()
    for i in bina:
        if i == '0':
            flip += '1'
        else:
            flip += '0'
    return int(flip, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
