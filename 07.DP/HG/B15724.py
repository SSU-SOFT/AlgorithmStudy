import sys
input = sys.stdin.readline

def pprint(arr):
    for line in arr:
        print(line)

N, M = map(int, input().split())

people = []
dp = [[0]*(M+1)]

for _ in range(N):
    tmp = list(map(int, input().split()))
    people.append(tmp)
    temp = [0]
    cnt = 0
    for n in tmp:
        cnt += n
        temp.append(cnt)
    for i in range(len(temp)):
        if dp:
            temp[i] += dp[-1][i]
    dp.append(temp)

K = int(input())

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)