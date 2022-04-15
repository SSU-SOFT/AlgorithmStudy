n = int(input())
for _ in range(n):
    N, M = input().split(" ")
    q = list(enumerate(map(int, input().split(" "))))
    out = []
    
    while q:
        cur = q.pop(0)
        isPrint = True
        for item in q:
            if cur[1] < item[1]:
                isPrint = False
                break
        if isPrint:
            out.append(cur)
        else:
            q.append(cur)
        
    #print(n, out)
    for idx, value in enumerate(out):
        if value[0] == int(M):
            print(idx+1)
            break