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
import heapq as hq

N, M = map(int, sys.stdin.readline().split(" "))
W = [[float('inf')] * N for _ in range(N)]
global parent
parent = [i for i in range(N)]

h = []
for _ in range(M):
    i, j, w = map(int, sys.stdin.readline().split(" "))
    hq.heappush(h, (w, i, j))

print(h)

def findRoot(x):
    if parent[x] == x:
        return x
    parent[x] = findRoot(parent[x])
    return parent[x]

def union(u, v):
    root1 = findRoot(u)
    root2 = findRoot(v)
    parent[root2] = root1

def Kruskal(heap):
    answer = []    
    while len(answer) < (N-1) and heap:
        w, i, j = hq.heappop(heap)
        print(w, i, j)
        
        if findRoot(i) == findRoot(j):
            continue
        
        union(i, j)
        answer.append((i, j, w))
        #setRoot
        print(parent)

    return answer

print(Kruskal(h))
