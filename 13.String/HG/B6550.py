import sys
input = sys.stdin.readline

while True:
    try:
        s, t = input().split()
        i = 0
        for ch in t:
            if s[i] == ch:
                i += 1
                if i == len(s):
                    break

        if i == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break
