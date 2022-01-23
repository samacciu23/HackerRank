'''
DESCRIPTION:
Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
Debug the given function strings_xor to find the XOR of the two given strings appropriately.
SAMPLE INPUT:
10101
00101
SAMPLE OUTPUT:
10000
'''
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))



