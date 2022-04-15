import sys
from collections import deque
input = sys.stdin.readline


def pprint(arr):
    for line in arr:
        print(line)

def bfs(a, b, area):
    result = set()
    q = deque([(a, b)])
    
    mx = [1, 0, -1, 0]  
    my = [0, 1, 0, -1]

    while q:
        x, y = q.pop()
        Apartment[x][y] = area
        visited[x][y] = True

        result.add((x, y))

        for i in range(4):
            tx = x + mx[i]
            ty = y + my[i]

            if 0 <= tx < N and 0 <= ty < N:
                if not visited[tx][ty] and Apartment[tx][ty] == '1':
                    q.append((tx, ty))

    return len(result)

def sol():
    answer = []
    cnt = 0
    global Apartment, visited, N
    N = int(input())
    Apartment = []
    visited = [[False] * N for _ in range(N)]
    for _ in range(N):
        Apartment.append(list(input().strip()))

    for x in range(N):
        for y in range(N):
            if not visited[x][y]: # 방문하지 않은 곳
                if Apartment[x][y] == '0': # 집이 없는 경우
                    visited[x][y] = True
                    continue
                elif Apartment[x][y] == '1': # 집이 있는 경우
                    answer.append(bfs(x, y, cnt))
                    cnt += 1
                    # pprint(Apartment)
    
    print(cnt)
    for n in sorted(answer):
        print(n)

sol()