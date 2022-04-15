import sys


def sol():
    N, M = map(int, sys.stdin.readline().strip().split(" "))
    answer = 0
    S = {}
    for _ in range(N):
        string = sys.stdin.readline().strip()
        S[string] = True

    for _ in range(M):
        string = sys.stdin.readline().strip()
        if string in S:
            answer += 1

    return answer
print(sol())