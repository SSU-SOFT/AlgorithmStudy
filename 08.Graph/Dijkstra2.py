# 6 10
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 4 3
# 3 5 1
# 3 6 5
# 4 5 1
# 5 6 2
import sys

N, M = map(int, input().split(" "))
G = [[0]* (N+1) for _ in range(N+1)]

def pprint(arr):
    for line in arr:
        print(line)

for _ in range(M):
    v1, v2, cost = map(int,sys.stdin.readline().split(" "))    
    G[v1][v2] = cost
    G[v2][v1] = cost


for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            G[i][j] = 0
        elif G[i][j] == 0:
            G[i][j] = float('inf')

pprint(G)

def Dijkstra(G, source):
    # init
    D = [float('inf') for _ in range(N+1)]    
    for i in range(N+1):
        if G[source][i] != 0:
            D[i] = G[source][i]
    visited = [False for _ in range(1+N)]
    D[source] = 0
    visited[0] = True
    visited[source] = True
    
    print("=================")
    while False in visited:
        # find min value
        idx = 0
        min = float('inf')
        for i in range(N+1):
            if D[i] < min and not visited[i]:
                min = D[i]
                idx = i
        
        print(idx, min)
        visited[idx] = True
        for j in range(1, N+1):
            print(j, visited[j])
            if not visited[j]:
                print(D[idx] + G[idx][j], D[j])
                if D[idx] + G[idx][j] < D[j]:
                    D[j] = D[idx] + G[idx][j]
        print(D)
    return D
Dijkstra(G, 1)
