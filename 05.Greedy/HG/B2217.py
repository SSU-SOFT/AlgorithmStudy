import sys
N = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(N)]
ropes = sorted(ropes, reverse=True)
maxValue = 0
minRope = float('inf')

for i in range(0, N):
    minRope = min(minRope, ropes[i])
    if maxValue < minRope * (i+1):
        maxValue = minRope * (i+1)

print(maxValue)
        
