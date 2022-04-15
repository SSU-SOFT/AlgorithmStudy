import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomato = []
isClear = False
q = deque()

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    tomato.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 1:
            q.append((i, j, 0))

def pprint(arr):
    for line in arr:
        print(line)

def check(tomato):
    for line in tomato:
        if 0 in line:
            return False
    return True

# pprint(tomato)
# print(q)

def sol(): 
    if check(tomato):
        print(0)
        return

    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]
    cnt = 0
    while q:
        x, y, d = q.popleft()
        cnt = d
        
        for i in range(4):
            tx = x + mx[i]
            ty = y + my[i]
            if 0 <= tx < N and 0 <= ty < M:
                if tomato[tx][ty] == 0:
                    tomato[tx][ty] = 1
                    q.append((tx, ty, d+1))
        # pprint(tomato)
        # print(q)


    if check(tomato):
        print(cnt)
    else:
        print(-1)
    return

sol()