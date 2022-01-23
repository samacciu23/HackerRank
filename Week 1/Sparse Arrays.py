'''
DESCRIPTION:
There is a collection of input strings and a collection of query strings.
For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
SAMPLE INPUT:
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
SAMPLE OUTPUT:
2
1
0
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2] == 'A':
        if s[:2] == '12':
            return '00'+s[2:8]
        else:
            return s[:8]
    else:
        if s[:2] == '12':
            return s[:8]
        else:
            h = int(s[:2])+12
            return str(h)+':'+s[3:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
