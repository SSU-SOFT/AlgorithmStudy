n = int(input())

def sol(price):
    cnt = 0
    while price > 0:
        if price % 5 == 0:
            print(price // 5 + cnt)
            return
        cnt+=1
        price -= 2
        
    if price == 0:
        print(cnt)
    else:
        print(-1)
    return
sol(n)