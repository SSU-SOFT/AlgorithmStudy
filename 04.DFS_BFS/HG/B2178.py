import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

def pprint(arr):
    for line in arr:
        print(line)

def bfs():
    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]
    q = deque([(0,0,1)])
    visited = [(0,0)]
    cnt = 0
    while q:
        x, y, c = q.popleft()
        cnt = max(cnt, c)
        if x == N-1 and y == M-1:
            break
        for i in range(4):
            tx = x + mx[i]
            ty = y + my[i]
            if 0 <= tx < N and 0 <= ty < M:
                if not (tx, ty) in visited and mage[tx][ty] == 1:
                    visited.append((tx, ty))
                    q.append((tx, ty, c+1))
    return cnt
mage = []
for _ in range(N):
    mage.append(list(map(int, list(sys.stdin.readline().rstrip()))))
print(bfs())