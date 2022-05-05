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
mid = 0
location = 1
R = 0
for _ in range(N):
    i, a = map(int, input().split())
    X[i] = a
    R += abs(i-location) * a # 새로 들어온 사람 거리 합
    tmpL = L + mid
    if tmpL < R:
        location += 1
        L = tmpL
        
    #         print(L, R)
    # print(L, location, R)
print(location)