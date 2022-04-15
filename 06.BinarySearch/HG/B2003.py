import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
# print("===================")

s = 0
e = 0
answer = 0
tmp = arr[s]

while s < N and e < N:
    if tmp < M:
        if e+1 >= N:
            break
        tmp += arr[e+1]
        e += 1
    elif tmp == M:
        answer += 1
        if e+1 >= N:
            break
        tmp += arr[e+1]
        e += 1
    else:
        tmp -= arr[s]
        s += 1
    # print(s, e, tmp, answer)

print(answer)