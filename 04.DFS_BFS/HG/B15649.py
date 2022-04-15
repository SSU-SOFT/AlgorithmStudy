import sys
global M
N, M = map(int, sys.stdin.readline().split())
global visited

visited = []

def dfs(cur, cnt):
    # check in 
    visited.append(str(cur))

    # Is Goal?
    if cnt < M:
        for nxt in range(1, N+1):
            if str(nxt) not in visited:
                dfs(nxt, cnt+1)
    else:
        print(" ".join(visited))
    
    visited.remove(str(cur))

    return 

for i in range(1, N+1):
    dfs(i, 1)