import heapq as hq
import sys
N = int(input())
h = []
#print(h)
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0: #출력
        if len(h) < 1:
            print(0)
        else:
            print(hq.heappop(h)[1])
    else:
        hq.heappush(h, (-x, x)) #append
    
        