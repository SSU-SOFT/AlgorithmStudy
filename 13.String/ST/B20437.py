import sys
import string

input = sys.stdin.readline
T = int(input())
alpha = list(string.ascii_lowercase)

for i in range(T):
    max = 0
    min = 10000
    alpha_count = {}
    W = list(input().strip())
    K = int(input())
    for a in alpha:
        if(W.count(a) >= K):
            alpha_count[a] = W.count(a)
    for a in alpha_count.keys():
        pos = [i for i in range(len(W)) if W[i]==a]
        for j in range(alpha_count[a] - K + 1):
            length = pos[j+K-1] - pos[j] + 1
            if(max < length):
                max = length
            if(min > length):
                min = length

    if(max == 0 and min == 10000):
        print(-1)
    else:
        print(min, max)