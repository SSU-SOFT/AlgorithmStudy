from collections import deque
from collections import defaultdict
import sys

def bfs(start, N):
    result = 1
    q = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    while q:
        # print(q)
        cur = q.popleft()
        for nxt in com[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                result += 1

    return result

N, M = map(int, sys.stdin.readline().split())
com = defaultdict(list)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    com[B].append(A)

maxValue = 0
answer = []
for i in range(1, N+1):
    value = bfs(i, N)
    if value == maxValue:
        answer.append(i)
    elif value > maxValue:
        maxValue = value
        answer = [i]

print(*answer)