import sys
import heapq as hq
N, M = map(int, sys.stdin.readline().split(" "))

def sol(n, m):
    if N == 0:
        print(0)
        return 0
    books = list(map(int, sys.stdin.readline().split(" ")))

    cnt = 1
    weight = 0

    while books:
        cur = books.pop()
        if weight + cur > m:
            cnt += 1
            weight = 0
        weight += cur
    print(cnt)
    return

sol(N, M)