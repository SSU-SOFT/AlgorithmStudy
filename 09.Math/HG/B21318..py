import sys
input = sys.stdin.readline

N = int(input())
levels = [0] + list(map(int, input().split()))
rise = [0]
for i in range(1, len(levels)):
    if levels[i] - levels[i-1] < 0:
        rise.append(rise[-1]+1)
    else:
        rise.append(rise[-1])

# print(rise)           

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(rise[y] - rise[x])