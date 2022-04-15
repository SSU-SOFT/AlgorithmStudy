import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

l, r = 0, 0
maxValue = 0
cnt = 0
while l <= r and r < N:
    if cnt < K:
        if S[r] % 2 != 0: 
            cnt += 1
        r += 1
        maxValue = max(maxValue, r-l-cnt)
    else:
        if S[r] % 2 == 0: # cnt가 K일때 짝수가 들어오는 경우
            r += 1
            maxValue = max(maxValue, r-l-cnt)
        else: #홀수가 들어오는 경우
            if S[l] % 2 != 0: #S[l]을 제거
                cnt -= 1
            l += 1
    
    # print(l, r, cnt)
    # print(S[l:r])

print(maxValue)
