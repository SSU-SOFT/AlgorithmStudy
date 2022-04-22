def solution(n, k, cmd):
    stack = []
    for i in range(len(cmd)):
        print(k, cmd[i], end = ' -> ')
        alpha = cmd[i].split()[0]
        if(alpha == 'D'):
            k += int(cmd[i].split()[1])
            if(k >= n):
                k = n-1
        elif(alpha == 'U'):
            k -= int(cmd[i].split()[1])
            if(k < 0):
                k = 0
        elif(alpha == 'C'):
            stack.append(k)
            n -= 1
            if(k >= n):
                k = n-1
        elif(alpha == 'Z'):
            restore_num = stack[-1]
            stack.pop()
            if(k >= restore_num):
                k += 1
            n += 1
        print(k)
        print(stack)
    answer = list('O' * n)
    stack.sort()
    for index in stack:
        answer.insert(index, 'X')
    return "".join(answer)
print(solution(8, 2,["C", "D 1", "C", "C"]))
