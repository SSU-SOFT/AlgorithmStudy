def solution(board, moves):
    answer = 0
    stack = []
    # pprint(board)
    for move in moves:
        num=0
        # num 뽑기
        for j in range(len(board)):
            if not board[j][move-1] == 0:
                num = board[j][move-1]
                board[j][move-1] = 0
                break
        # num을 stack에 비교하기
        if not num == 0:
            if len(stack) > 0 and stack[-1] == num:
                answer += 2
                stack.pop()
            else:
                stack.append(num)
    # print(stack)
    return answer

def pprint(arr):
    for i in arr:
        print(i)