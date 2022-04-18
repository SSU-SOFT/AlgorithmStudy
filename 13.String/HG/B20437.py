import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    W = input().strip()
    K = int(input())
    alpIdx = defaultdict(list)
    candidate = set()
    for idx, ch in enumerate(W):
        alpIdx[ch].append(idx)
        if len(alpIdx[ch]) >= K:
            candidate.add(ch)

    if not candidate:
        print(-1)
        continue

    minValue = float('inf')
    maxValue = 0

    for ch in candidate:
        arr = alpIdx[ch]
        size = K-1
        for i in range(len(arr)- size):
            length = (arr[i+size]+1 - arr[i])
            minValue = min(length, minValue)
            maxValue = max(length, maxValue)

    print(minValue, maxValue)