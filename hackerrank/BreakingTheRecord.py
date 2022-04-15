#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    result = [0, 0]
    minValue = scores[0]
    MaxValue = scores[0]
    for score in scores[1:]:
        if score < minValue:
            minValue = score
            result[1] += 1
        if score > MaxValue:
            MaxValue = score
            result[0] += 1
            
        # print(minValue, MaxValue)
        
    return result
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
