import sys
import itertools as it
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a%b)


t = int(input())
for _ in range(t):
    case = input().strip().split(" ")
    n = case[0]
    result = 0
    for a, b in it.combinations(case[1:], 2):
        # print(a,b)
        # print(gcd(a,b))
        result += gcd(int(a), int(b))
    print(result)
