'''
DESCRIPTION:
You will be given a list of integers, arr, and a single integer k.
You must create an array of length k from elements of arr such that
its unfairness is minimized. Call that array arr1.
Unfairness of an array is calculated as
max(arr1)-min(arr1)
Where:
- max denotes the largest integer in arr1.
- min denotes the smallest integer in arr1.
EXAMPLE:
arr = [1,4,7,2]
k = 2
Pick any two elements, say arr1 = [4,7].
unfairness = max(4,7) - min(4,7) = 7-4 = 3.
Testing for all pairs, the solution [1,2] provides the minimum unfairness.
Note: Integers in arr may not be unique.
'''

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    results = []
    for i in range(len(arr) + 1 - k):
        unfairness = arr[i + k - 1] - arr[i]
        results.append(unfairness)
    return min(results)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
