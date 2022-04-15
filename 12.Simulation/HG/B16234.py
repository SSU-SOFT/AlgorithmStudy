from collections import deque
import sys
input = sys.stdin.readline


def pprint(arr):
    for line in arr:
        print(line)

def bfs(a, b):
    result = []
    
    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]

    q = deque([(a, b)])
    sumValue = 0

    while q:
        x, y = q.popleft()
        
        if (x, y) not in result:
            sumValue += population[x][y]
            result.append((x, y))
        
        visited[x][y] = True
    
        for i in range(4):
            tx = x + mx[i]
            ty = y + my[i]
            
            if 0 <= tx < N and 0 <= ty < N:
                if not visited[tx][ty] and L <= abs(population[x][y] - population[tx][ty]) <= R:
                    q.append((tx, ty))
        
    return sumValue, result

def sol():
    global N, L, R
    N, L, R = map(int, input().split())
    answer = 0
    global population, visited
    population = []
    
    for _ in range(N):
        arr = list(map(int, input().split()))
        population.append(arr)
    
    while True:
        visited = [[False] * N for _ in range(N)]
        uni = []

        mx = [1, 0, -1, 0]
        my = [0, 1, 0, -1]

        for x in range(N):
            for y in range(N):
                if not visited[x][y]:
                    needBFS = False

                    for i in range(4):
                        tx = x + mx[i]
                        ty = y + my[i]

                        if 0 <= tx < N and 0 <= ty < N:
                            if not visited[tx][ty] and L <= abs(population[x][y] - population[tx][ty]) <= R:
                                needBFS = True
                                break
                    
                    if needBFS:
                        print(x,y)
                        uni.append(bfs(x, y))

        # print(uni)
        if len(uni) == N**2:
            break

        for value, pos in uni:
            if len(pos) > 1:
                uniPeoples = value // len(pos)
                for a, b in pos:
                    population[a][b] = uniPeoples

        # pprint(population)
        answer += 1
    
    return answer

print(sol())