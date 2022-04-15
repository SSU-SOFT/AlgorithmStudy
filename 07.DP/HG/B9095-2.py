import sys
import itertools as it
T = int(input())
DP = [0] * 11
DP[1] = 1
DP[2] = 2
DP[3] = 4

for _ in range(T):
    n = int(sys.stdin.readline())
    for j in range(4, n+1):
        DP[j] = DP[j-1] + DP[j-2]+ DP[j-3]
    print(DP[n])
    