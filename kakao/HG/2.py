from collections import deque
def solution(queue1, queue2):
    answer = 0
    N = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    while q1 and q2 and cnt <= N*2:
        if sum1 == sum2:
            break
        if sum1 > sum2:
            num = q1.popleft()
            sum1 -= num
            sum2 += num
            q2.append(num)
        else:
            num = q2.popleft()
            sum2 -= num
            sum1 += num
            q1.append(num)
        cnt += 1
        # print(q1, q2)
    # print(sum1, sum2, cnt)
    
    if cnt >= N*2 or not q1 or not q2:
        answer = -1
    else:
        answer = cnt

    return answer