import sys
M, N = map(int, sys.stdin.readline().split(" "))

board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

def pprint(arr):
    for line in arr:
        print(line)

pprint(board)


