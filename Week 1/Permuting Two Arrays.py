'''
DESCRIPTION:
There are two n-element arrays of integers, A and B.
Permute them into some A' and B' such that
the relation A'[i]+B'[i]>=k holds for all i where 0<=i<n.
There will be q queries consisting of A, B, and k.
For each query, return YES if some permutation A', B'
satisfying the relation exists. Otherwise, return NO.
SAMPLE INPUT:
STDIN       Function
-----       --------
2           q = 2
3 10        A[] and B[] size n = 3, k = 10
2 1 3       A = [2, 1, 3]
7 8 9       B = [7, 8, 9]
4 5         A[] and B[] size n = 4, k = 5
1 2 2 1     A = [1, 2, 2, 1]
3 3 3 4     B = [3, 3, 3, 4]
SAMPLE OUTPUT:
YES
NO
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    i = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    print(A, B)
    while i < len(A):
        if A[i]+B[i]>=k:
            pass
        else:
            return 'NO'
        i+=1
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
