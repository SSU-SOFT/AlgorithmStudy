#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    answer = 0
    l = 0
    r = 0
    
    while l <= r and r <= len(s):
        tmp = sum(s[l:r])
        if tmp < d:
            r += 1
        elif tmp > d:
            l += 1
        else:
            # print(l, r)
            # print(s[l:r])
            if r-l == m:
                answer += 1
            r += 1
    
    return answer
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
