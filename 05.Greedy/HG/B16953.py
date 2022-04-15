A, B = map(int, input().split())

global answer
answer = float('inf')

def sol(n, goal, cnt):
    # print(n)
    if n == goal:
        return cnt
    elif n < goal:
        return min(answer, sol(2*n, goal, cnt+1), sol(10*n+1, goal, cnt+1))
    else:
        return float('inf')

answer = sol(A, B, 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer+1)