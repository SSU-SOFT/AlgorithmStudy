import sys
from collections import deque
from collections import defaultdict

N, M = map(int, sys.stdin.readline().strip().split())
indegree = [0 for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
g = defaultdict(list)
q = deque([])
visited = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    indegree[b] += 1
    g[a].append(b)

# print(indegree)
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append((i, 1))
        answer[i] = 1

while q:
    cur, cnt = q.popleft()
    for nxt in g[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append((nxt, cnt+1))
            answer[nxt] = cnt+1

print(*answer[1:])