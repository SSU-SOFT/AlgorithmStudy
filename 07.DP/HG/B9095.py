import sys
import itertools as it
T = int(input())
cnt = 0

def sol(sum, goal):
    answer = 0
    if sum > goal:
        return 0
    elif sum == goal:
        return 1
    else:
        for i in range(1, 4):
            answer += sol(sum+i, goal)

    return answer


for _ in range(T):
    n = int(sys.stdin.readline())
    print(sol(0, n))   