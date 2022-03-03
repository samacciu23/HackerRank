'''
DESCRIPTION:
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters.
If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
EXAMPLE:
s = There's-a-starman-waiting-in-the-sky
k = 3
The alphabet is rotated by 3, matching the mapping above. The encrypted string is
Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb.
Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    lst_string = list(map(lambda x: x, s))
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    upper_rotated = list(string.ascii_uppercase)
    lower_rotated = list(string.ascii_lowercase)
    for _ in range(k):
        upper_rotated.append(upper_rotated.pop(0))
        lower_rotated.append(lower_rotated.pop(0))
    for i in range(len(s)):
        if lst_string[i] in upper:
            lst_string[i] = upper_rotated[upper.index(lst_string[i])]
        if lst_string[i] in lower:
            lst_string[i] = lower_rotated[lower.index(lst_string[i])]
    return ''.join(lst_string)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
