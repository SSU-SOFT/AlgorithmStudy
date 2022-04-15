def solution(n, times):
    answer = 0
    low = 0
    high = 1000000000*1000000000
    while True:
        if low > high:
            break
        mid = (low+high) // 2
        value = 0
        for time in times:
            value += mid // time
        # print(value, mid)
        if value >= n:
            answer = mid
            high = mid-1
        elif value < n:
            low = mid+1
    
    return answer