import sys
input = sys.stdin.readline
A, B, C, M = map(int, input().split())
fatig = 0
work = 0
for _ in range(24):
    if(fatig + A <= M):
        fatig += A
        work += B
    else:
        fatig -= C
    if(fatig < 0):
        fatig = 0
print(work)