import pprint as pp
import sys
from collections import deque
input = sys.stdin.readline

def copyWater(r, c):
    cnt = 0
    mx = [1, 1, -1, -1]
    my = [-1, 1, 1, -1]

    for i in range(4):
        tx = r+mx[i]
        ty = c+my[i]
        if tx < 0 or N <= tx or ty < 0 or N <= ty:
            continue
        if A[tx][ty] > 0:
            cnt += 1
    A[r][c] += cnt
    return

def sol():
    global N, A
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    # pp.pprint(A)
    mx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    my = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    clouds = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

    for _ in range(M):
        d, s = map(int, input().split())
        # print(mx[d]*s, my[d]*s)
        l = len(clouds)

        for _ in range(l):
            r, c = clouds.popleft()
            tx = (r + mx[d]*s) % N
            ty = (c + my[d]*s) % N
            # print(tx, ty, end="|")
            A[tx][ty] += 1
            clouds.append((tx, ty))
        # print()

        # pp.pprint(A)
        visited = [[False] * N for _ in range(N)]
        for r, c in clouds:
            # print(r, c, end="|")
            copyWater(r, c)
            visited[r][c] = True
        # print("\n# copyWater")
        # pp.pprint(A)
        # pp.pprint(visited)
        tmp = deque([])
        for i in range(N):
            for j in range(N):
                if A[i][j] >= 2 and not visited[i][j]:
                    A[i][j] -= 2
                    tmp.append((i, j))
        clouds = tmp
        # pp.pprint(A)
    print(sum(sum(b) for b in A))
sol()