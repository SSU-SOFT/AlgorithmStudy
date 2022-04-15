N = input()

def solution(N):
    if int(N) < 19:
        start = 1
    else:
        start = int(N) - len(N)*9
    answer = 0

    for num in range(start, int(N)):
        result = num
        tmp = 0
        while num:
            tmp += num % 10
            num = num // 10
        
        # print(result, tmp)

        if result + tmp == int(N):
            answer = result
            break

    return answer

print(solution(N))