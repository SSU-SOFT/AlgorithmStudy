import sys
input = sys.stdin.readline
import heapq as hq
def pprint(arr):
    for line in arr:
        print(line)

V, E = map(int, input().split())
h = []
parent = [i for i in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    hq.heappush(h, (C, A, B))
# pprint(graph)0

# for i in range(V):
#     graph[i][i] = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    parent[root2] = root1

def kruskal(heap):
    answer = 0
    cnt = 0

    while cnt < (V-1) and heap:
        c, a, b = hq.heappop(heap)
        if find(a) == find(b):
            continue

        union(a, b)
        answer += c
        cnt += 1

    return answer

print(kruskal(h))