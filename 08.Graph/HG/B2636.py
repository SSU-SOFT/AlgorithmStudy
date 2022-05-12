import sys
input = sys.stdin.readline
import pprint as pp
from collections import deque

H, W = map(int, input().split())
global visited
visited = [[0] * W for _ in range(H)]
N = 0
cheese = []
for _ in range(H):
    tmp = list(map(int, input().split()))
    cheese.append(tmp)
    N += tmp.count(1)

# pp.pprint(cheese)
# print(N)

mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
cnt = 0

def bfs(start, N):
    cur = 0
    cnt = 2
    n = 0
    q = [start]
    while cur < N:
        outline = []
        while q:
            x, y = q.pop()
            visited[x][y] = -1
            cheese[x][y] = -1
            for i in range(4):
                tx = x + mx[i]
                ty = y + my[i]

                if 0 <= tx < H and 0 <= ty < W and visited[tx][ty] == 0:
                    if cheese[tx][ty] == 0:
                        q.append((tx, ty))
                    elif cheese[tx][ty] == 1:
                        visited[tx][ty] = cnt
                        outline.append((tx, ty))
        # pp.pprint(visited)
        n = len(outline)
        cur += n
        # print(cur, n)
        q = outline
        cnt += 1
    # check out line
    print(cnt-2)
    print(n)



bfs((0, 0), N)