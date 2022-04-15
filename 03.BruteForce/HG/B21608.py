import sys

def pprint(arr):
    for line in arr[1:]:
        print(line[1:])

def sol():
    answer = 0
    N = int(sys.stdin.readline().strip())
    sit = [[0] * (N+1) for _ in range(N+1)]

    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]

    likes = {}
    
    for _ in range(N**2):
        p, like = sys.stdin.readline().strip().split(" ", 1)
        likes[p] = like.split(" ")

        results = []
        MaxValue = 0
                    
        for x in range(1, N+1):
            for y in range(1, N+1):
                if sit[x][y] == 0:
                    LikeCnt = 0
                    EmptyCnt = 0
                    #순회
                    for i in range(4):
                        tx = x + mx[i]
                        ty = y + my[i]
                        if 0 < tx <= N and 0 < ty <= N:
                            if sit[tx][ty] in likes[p]:
                                LikeCnt += 1
                            elif sit[tx][ty] == 0:
                                EmptyCnt += 1

                        if LikeCnt > MaxValue:
                            MaxValue = LikeCnt
                            results = [(EmptyCnt, x, y)]
                        elif LikeCnt == MaxValue:
                            results.append((EmptyCnt, x, y))


        # print(MaxValue, sorted(results, key=lambda x: (-x[0], -x[1], x[2], x[3])))
        emptyCnt, x, y = sorted(results, key=lambda x: (-x[0], x[1], x[2]))[0]
        
        # print(cnt, x, y)
        sit[x][y] = p
    # pprint(sit)
    score = {0: 0, 1: 1, 2:10, 3:100, 4:1000}
    # print(likes)
    for x in range(1, N+1):
        for y in range(1, N+1):
            cnt = 0
            for i in range(4):
                tx = x + mx[i]
                ty = y + my[i]
                if 0 < tx <= N and 0 < ty <= N:
                    if sit[tx][ty] in likes[sit[x][y]]:
                        cnt += 1
            answer += score[cnt]
            # print(cnt)
    return answer
print(sol())