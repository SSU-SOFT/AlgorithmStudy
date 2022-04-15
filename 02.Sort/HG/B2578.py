import sys
import pprint

def pprint(arr):
    for line in arr:
        print(line)

def check(board, row, col, diag):
    # row
    for i, line in enumerate(board):
        if sum(line) == 0:
            row[i] = 1
    # col
    for i, line in enumerate(zip(*board)):
        if sum(line) == 0:
            col[i] = 1
    # diag
    cnt1 = 0
    cnt2 = 0
    for i in range(len(board)):
        cnt1 += board[i][i]
        cnt2 += board[len(board)-1-i][i]

    if cnt1 == 0:
        diag[0] = 1
    if cnt2 == 0:
        diag[1] = 1

    if sum(row)+sum(col)+sum(diag) >= 3:
        return True
    else:
        return False

bingo1 = []
bingo2 = []
pos = {}
row = [0,0,0,0,0]
col = [0,0,0,0,0]
diag = [0, 0]
for i in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    bingo1.append(nums)
    for j, num in enumerate(nums):
        pos[num] = (i, j)

for i in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    bingo2.extend(nums)

# print(bingo2)

for i, num in enumerate(bingo2):
    x, y = pos[num]
    bingo1[x][y] = 0
    if check(bingo1, row, col, diag):
        print(i+1)
        break

# pprint(bingo1)

