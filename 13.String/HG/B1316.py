import sys
input = sys.stdin.readline
N = int(input()) # input의 return 값은 string
answer = 0

for _ in range(N):
    cnt = {}
    result = True
    word = input().strip()
    tmp = None
    for ch in word:
        if not cnt.get(ch):
            cnt[ch] = True
            tmp = ch
        else:
            if tmp == ch:
                continue
            else:
                result = False
                break
    if result:
        answer += 1

print(answer)

    