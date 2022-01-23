'''
DESCRIPTION:
A pangram is a string that contains every letter of the alphabet.
Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case. Return either pangram or not pangram as appropriate.
SAMPLE INPUT:
We promptly judged antique ivory buckles for the next prize.
SAMPLE OUTPUT:
pangram
'''
# !/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()
    for l in list(string.ascii_lowercase):
        if l in s:
            pass
        else:
            return 'not pangram'
    return 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
