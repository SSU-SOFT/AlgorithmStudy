import sys
input = sys.stdin.readline
W, H = map(int, input().split())
sys.setrecursionlimit(100000)
data = []
for i in range(H):
    data.append(list(map(int, input().split())))

def find_outline(x, y):
    if(data[y][x] == 0):
        data[y][x] = -1
        if(x != W-1):
            find_outline(x+1, y)
        if(x != 0):
            find_outline(x-1, y)
        if(y != H-1):
            find_outline(x, y+1)
        if(y != 0):
            find_outline(x, y-1)
        if(y % 2 == 0):
            if(x != W-1 and y != H-1):
                find_outline(x+1, y+1)
            if(x != W-1 and y != 0):
                find_outline(x+1, y-1)
        else:
            if(x != 0 and y != H-1):
                find_outline(x-1, y+1)
            if(x != 0 and y != 0):
                find_outline(x-1, y-1)

for x in range(W):
    find_outline(x, 0)
    find_outline(x, H-1)
for y in range(H):
    find_outline(0, y)
    find_outline(W-1, y)

ans = 0
def count_light(x, y):
    count = 0
    
    if(y != H-1):
        if(data[y+1][x] >= 0):
            count += 1
    if(y != 0):
        if(data[y-1][x] >= 0):
            count += 1
    if(x != W-1):
        if(data[y][x+1] >= 0):
            count += 1
    if(x != 0):
        if(data[y][x-1] >= 0):
            count += 1
    
    if(y % 2 == 0):
        if(y != H-1 and x != W-1):
            if(data[y+1][x+1] >= 0):
                count += 1
        if(y != 0 and x != W-1):
            if(data[y-1][x+1] >= 0):
                count += 1
    else:
        if(y != H-1 and x != 0):
            if(data[y+1][x-1] >= 0):
                count += 1
        if(y != 0 and x != 0):
            if(data[y-1][x-1] >= 0):
                count += 1
    return 6-count

for y in range(H):
    for x in range(W):
        if(data[y][x] == 1):
            ans += count_light(x, y)

print(ans)