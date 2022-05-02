# 4
# 1 1
# 2 2
# 3 3
# 4 4

# 5
# 1 4
# 2 2
# 3 0
# 4 4
# 5 3
import sys
input = sys.stdin.readline

N = int(input())
X = [0] * (N+1)
L = 0
location = 1
R = 0
for _ in range(N):
    i, a = map(int, input().split())
    X[i] = a
    R += abs(i-location) * a # 새로 들어온 사람 거리 합
    if L < R: # 왼쪽보다 크다면 location을 키워 최대한 맞춤.
        while L < R:
            location += 1
            L, R = 0, 0
            for j in range(1, location):
                L += abs(j-location) * X[j]
            for k in range(location, len(X)):
                R += abs(k-location) * X[k]
    #         print(L, R)
    # print(L, location, R)
print(location)