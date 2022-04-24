from collections import deque
import sys
input = sys.stdin.readline

def pprint(arr):
    for line in arr:
        print(line)
        

W, H = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]

visited = [[False] * W for _ in range(H)]
Inside = [[0] * W for _ in range(H)]

mx = [-1, -1, 0, 0, 1, 1]
my1 = [-1, 0, -1, 1, -1, 0]
my2 = [0, 1, -1, 1, 0, 1]

def IsInside(x, y):
    result = True
    q = deque([(x, y)])

    if Inside[x][y] != 0: #DP
        if Inside[x][y] == 1: # Inside
            return True
        elif Inside[x][y] == -1: # OutSide
            return False
    
    tmp = []

    while q:
        r, c = q.popleft()
        tmp.append((r, c))

        for i in range(6):
            row = r + mx[i]
            
            if row % 2 == 0: # row is Even
                col = c + my1[i]
            else:            # row is Odd
                col = c + my2[i]
            
            # Index를 넘어가는 경우 outside
            if row < 0 or H <= row or col < 0 or W <= col:
                result = False
                continue

            if not (row, col) in tmp and G[row][col] == 0:
                q.append((row, col))
    
    if result:
        for x, y in tmp:
            Inside[x][y] = 1
    else:
        for x, y in tmp:
            Inside[x][y] = -1
    return result

def bfs(start):
    result = 0
    q = deque([start])

    while q:
        rounds = 0
        r, c = q.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True
        for i in range(6):
            row = r + mx[i]
            
            if row % 2 == 0: # row is Even
                col = c + my1[i]
            else:            # row is Odd
                col = c + my2[i]

            # Index를 넘어가는 경우 둘레 +1
            if row < 0 or H <= row or col < 0 or W <= col:
                # print(row, col)
                rounds += 1
                continue

            # Index를 넘어가지 않는 경우
            if not visited[row][col]:
                if G[row][col] > 0:
                    q.append((row, col))
                elif not IsInside(row, col):
                    rounds += 1
        
        G[r][c] = rounds
        result += rounds

    return result

answer = 0
for i in range(H):
    for j in range(W):
        if not visited[i][j] and G[i][j] == 1:
            answer += bfs((i, j))
print(answer)