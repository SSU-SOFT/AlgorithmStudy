import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())
answer = 0
state = 0
hour = 0

while hour < 24:
    if state + A <= M:
        answer += B
        state += A
    else:
        state -= C
        if state < 0:
            state = 0
    hour +=1
    # print(hour, answer, state)
print(answer)
