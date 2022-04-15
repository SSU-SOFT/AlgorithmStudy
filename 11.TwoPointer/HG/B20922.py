import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = list(map(int, input().split()))

cnt = [0] * 100001
maxValue=0
l, r = 0, 0
while l <= r and r < N:
    if cnt[a[r]]+1 <= K:
        cnt[a[r]] += 1
        r += 1
        maxValue = max(maxValue, r-l)
    else:
        cnt[a[l]] -= 1
        l += 1
    
print(maxValue)