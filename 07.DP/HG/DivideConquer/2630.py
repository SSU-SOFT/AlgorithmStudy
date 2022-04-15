import sys
N = int(input())
paper = []
global answer
answer = [0, 0]
def pprint(arr):
    for line in arr:
        print(line)

for _ in range(N):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    paper.append(line)


def sol(paper, n):
    cnt = sum(list(map(sum, paper)))
    if cnt == 0:
        answer[0] += 1
    elif cnt == n**2:
        answer[1] += 1
    else:
        mx = [0, 0, 1, 1]
        my = [0, 1, 0, 1]
        for i in range(4):
            tx = mx[i]*n//2
            ty = my[i]*n//2
            new_paper = []
            for j in range(tx,tx+n//2):
                new_paper.append(paper[j][ty:ty+n//2])
            sol(new_paper, n//2)

sol(paper, N)
print(answer[0])
print(answer[1])