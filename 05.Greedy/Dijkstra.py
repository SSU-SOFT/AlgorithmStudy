#Input
# 6 9
# 1 2 7
# 1 3 9
# 1 6 14
# 2 3 10
# 2 4 15
# 3 4 11
# 3 6 2
# 4 5 6
# 5 6 9
import sys

N, M = map(int, input().split(" "))
G = [[0]* (N+1) for _ in range(N+1)]

def pprint(arr):
    for line in arr:
        print(line)

visited = [0 for _ in range(1+N)]

for _ in range(M):
    v1, v2, cost = map(int,sys.stdin.readline().split(" "))    
    G[v1][v2] = cost
    G[v2][v1] = cost

pprint(G)

import heapq as hq

def Dijkstra(Graph, source):    
    queue = []
    
    dist = [float('inf') for _ in range(1+N)]
    dist[source] = 0

    hq.heappush(queue, (dist[source], source))
    
    while queue:
        print(queue)
        print(dist)
        cur_dist, cur_dest = hq.heappop(queue)
        if dist[cur_dest] < cur_dist: # 기존에 있는 거리보다 긴 경우
            continue

        for i in range(1, N+1):
            new_dest = i
            new_dist = G[cur_dest][new_dest]
            if new_dist != 0:
                distance = cur_dist + new_dist
                if distance < dist[new_dest]:
                    dist[new_dest] = distance
                    hq.heappush(queue, (distance, new_dest))
        
    
    return dist

answer = Dijkstra(G, 1)
print(answer)