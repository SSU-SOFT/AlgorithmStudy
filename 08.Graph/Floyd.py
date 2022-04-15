# input
# 5 6
# 0 1 2
# 0 2 3
# 1 4 10
# 2 4 4
# 2 3 1
# 3 4 2
import sys
import pprint as pp

V, E = map(int, sys.stdin.readline().split(" "))
W = [[0] * V for _ in range(V)]
D = []
for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split(" "))
    W[v1][v2] = cost
    W[v2][v1] = cost

for i in range(V):
    tmp = []
    for j in range(V):
        if i == j:
            tmp.append(0)
        elif W[i][j] != 0:
            tmp.append(W[i][j])
        else:
            tmp.append(float('inf'))
    D.append(tmp)

# pp.pprint(W)
pp.pprint(D)

for i in range(V):
    for j in range(V):
        for k in range(V):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

pp.pprint(D)
