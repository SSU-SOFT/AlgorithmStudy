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

def IsInside(start):
    st = [start]
    while st:
        r, c = st.pop()
        G[r][c] = -1
        if visited[r][c]:
            continue
        visited[r][c] == True

        for i in range(6):
            row = r + mx[i]
            if row % 2 == 0: # row is Even
                col = c + my1[i]
            else:            # row is Odd
                col = c + my2[i]
            # Index를 넘어가는 경우 outside
            if row < 0 or H <= row or col < 0 or W <= col:
                continue
            # Index를 넘어가지 않고 next node
            if not visited[row][col] and G[row][col] == 0:
                st.append((row, col))

def dfs(start):
    result = 0
    st = [start]

    while st:
        rounds = 0
        r, c = st.pop()
        
        #check in
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
                    st.append((row, col))
                elif G[row][col] < 0:
                    rounds += 1
        
        G[r][c] = rounds
        result += rounds

    return result

answer = 0

#Top & Bottom
for i in range(W):
    if not visited[0][i] and G[0][i] == 0:
        IsInside((0, i))
    if not visited[H-1][i] and G[H-1][i] == 0:
        IsInside((H-1, i))
    
# Left & Right
for i in range(H):
    if not visited[i][0] and G[i][0] == 0:
        IsInside((i, 0))
    if not visited[i][W-1] and G[i][W-1]==0:
        IsInside((i, W-1))
# pprint(G)
# print()
for i in range(H):
    for j in range(W):
        if not visited[i][j] and G[i][j] == 1:
            answer += dfs((i, j))
# pprint(G)
print(answer)