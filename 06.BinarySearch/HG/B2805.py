import sys
N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
Top = max(trees)



def bs(trees, value, low, high):    
    result = 0
    while True:
        if (low > high):
            break
        mid = int((low + high) / 2)
        h = []
        for item in trees:
            v = item - mid
            if v < 0:
                h.append(0)
            else:
                h.append(v)
        # print(mid, h)
        H = sum(h)
        if H > value:
            result = mid
            low = mid+1
        elif H < value :
            high = mid-1
        else:
            result = mid
            break
    print(result)
    return result
        
bs(trees, M, 0, Top)  
