import sys
from collections import deque
N, M, V = map(int, input().split())

G = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    G[i].append(j)
    G[j].append(i)

G = list(map(sorted, G))

def dfs(s):
    if s in visited:
        return
    print(s, end=" ")
    visited.append(s)
    for v in G[s]:
        if not v in visited:
            dfs(v)
    
# 역방향순으로 들어가야함.
# def dfs(G, s):
#     answer = ""
#     visited = [s]
#     st = [s]
#     while st:
#         cur = st.pop()
#         answer += str(cur)+" "
#         visited.append(cur)
#         for v in G[cur]:
#             if not v in visited:
#                 st.append(v)
#         print(st)
#     return answer

def bfs(s):
    q = deque([s])
    visited = [s]
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for v in G[cur]:
            if not v in visited:
                visited.append(v)
                q.append(v)
        # print(q)
visited=[]
dfs(V)
print()
bfs(V)