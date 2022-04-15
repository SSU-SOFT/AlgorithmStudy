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

N, M = map(int, sys.stdin.readline().split(" "))
W = [[float('inf')]*N for _ in range(N)]

for _ in range(M):
    i, j, w = map(int, sys.stdin.readline().split(" "))
    W[i][j] = w
    W[j][i] = w

for i in range(N):
    W[i][i] = 0

pprint(W)

def prim(G, source):
    # init
    answer = []
    dist = [G[source][i] for i in range(N)]
    nearest = [0 for _ in range(N)]

    print(dist)
    print(nearest)
    #find min idx
    
    while len(answer) < N:
        min = float('inf')
        vnear = 0
        for i in range(1, N):
            if 0 <= dist[i] < min:
                min = dist[i]
                vnear = i
        if min == float('inf') and vnear == 0:
            break
        print(min, vnear)
        # add answer
        answer.append((vnear, min))
        dist[vnear] = -1
        
        # renew
        for i in range(1, N):
            if G[i][vnear] < dist[i]:
                dist[i] = G[i][vnear]
                nearest[i] = vnear
        print(dist)
        print(nearest)

    return answer



print(prim(W, 0))