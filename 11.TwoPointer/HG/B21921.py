import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visited = list(map(int, input().split()))+[0]

idx = 0
cnt = 0
maxValue = 0
sumValue = sum(visited[idx:X])

while idx+X <= N:
    # print(maxValue, sumValue)
    if sumValue > maxValue:
        cnt = 1
        maxValue = sumValue
    elif sumValue == maxValue:
        cnt += 1

    sumValue -= visited[idx]
    sumValue += visited[idx+X]
    idx += 1
if maxValue == 0:
    print("SAD")
else:
    print(maxValue)
    print(cnt)
