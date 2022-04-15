def pprint(arr):
    for line in arr:
        print(line)

# 5 7
# 0 1 1
# 0 2 3
# 1 2 3
# 1 3 6
# 2 3 4
# 2 4 2
# 3 4 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a][b] = c
    G[b][a] = c 

for i in range(N):
    G[i][i] = 0

pprint(G)

def prim(G, source):
    answer = []
    dist = [G[source][i] for i in range(N)]
    nearest = [0] * N

    while len(answer) < N:
        minValue = float('inf')
        vnear = 0

        for i in range(N):
            if 0 < dist[i] < minValue:
                minValue = dist[i]
                vnear = i
        
        if minValue == float('inf') and vnear == 0:
            break
        
        answer.append((vnear, minValue))
        dist[vnear] = -1

        print(dist)
        print(vnear)

        #Update Dist
        for i in range(1, N):
            if G[i][vnear] < dist[i]:
                dist[i] = G[i][vnear]
                nearest[i] = vnear
    
    return answer


print(prim(G, 0))