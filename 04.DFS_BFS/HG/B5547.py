
import pprint as pp
from collections import deque
import sys
input = sys.stdin.readline

mx = [-1, -1, 0, 0, 1, 1]
my1 = [-1, 0, -1, 1, -1, 0]
my2 = [0, 1, -1, 1, 0, 1]

def isInside(start):
    result = True
    q = deque([start])
    tmp = []
    while q:
        r, c = q.popleft()
        print("Inside : ", r, c)
        tmp.append((r, c))
        for i in range(6):
            row = r + mx[i]
            if r % 2 == 0: #Even
                col = c + my2[i]    
            else: #Odd
                col = c + my1[i]
            
            if 0 <= row < H and 0 <= col < W:
                if Inside[row][col] == -1:
                    result = False
                    
                if G[row][col] == 1:
                    continue
                else:
                    print(row, col)
                    if Inside[row][col] == 0:
                        q.append((row, col))
            else:
                result = False
                break
    
    if result:
        for r, c in tmp:
            Inside[r][c] = 1
    else:
        for r, c in tmp:
            Inside[r][c] = -1

    return result

def bfs(start, cnt):
    result = 0
    q = deque([start])
    
    while q:
        x, y = q.popleft()
        print("current : ", x, y)
        rounds = 0
        for i in range(6):
            row = x + mx[i]
            if x % 2 == 0: #Even
                col = y + my2[i]    
            else: #Odd
                col = y + my1[i]
            
            if 0 <= row < H and 0 <= col < W:
                if not visited[row][col]:
                    if G[row][col] == 1:
                        visited[row][col] = True
                        q.append((row, col))
                    elif not isInside((row, col)):
                        print(row, col)
                        rounds += 1
            else:
                rounds += 1

        G[x][y] = rounds
        result += rounds
    return result
W, H = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
Inside = [[0] * W for _ in range(H)]

cnt = 2
starts = []
answer = 0
for i in range(H):
    for j in range(W):
        if not visited[i][j] and G[i][j] == 1:
            visited[i][j] = True
            tmp = bfs((i, j), cnt)
            print(tmp)
            answer += tmp
            cnt += 1

pp.pprint(G)
pp.pprint(visited)
pp.pprint(Inside)
print(answer)
