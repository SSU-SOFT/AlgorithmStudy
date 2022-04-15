#input
# 4 9
# 0 1 2
# 1 0 1
# 0 2 9
# 1 2 6
# 2 1 7
# 1 3 4
# 3 1 3
# 3 0 6
# 2 3 8
def pprint(arr):
    for line in arr:
        print(line)

N, M = map(int, input().split(" "))

W = [[0] * N for _ in range(N)]
D = []
for _ in range(M):
    v1, v2, cost = map(int, input().split(" "))
    W[v1][v2] = cost

for i in range(N):
    for j in range(N):
        if i == j:
            W[i][j] = 0
        elif W[i][j] == 0:
            W[i][j] = float('inf')

def travel():
    for i in range(1, N+1):
        D[i]
        


pprint(W)
