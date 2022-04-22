def solution(n, k, cmd):
    answer = ''
    HEAD = k
    table = [i for i in range(n)]
    last = n-1
    stack = []
    
    for command in cmd:
        # print(command)
        if command[0] == "U":
            C, X = command.split()
            cnt = 0
            while cnt < int(X):
                if table[HEAD] != -1:
                    cnt += 1
                HEAD -= 1
        elif command[0] == "D":
            C, X = command.split()
            cnt = 0
            while cnt < int(X):
                if table[HEAD] != -1:
                    cnt += 1
                HEAD += 1
        elif command[0] == "C":
            stack.append(table[HEAD])
            table[HEAD] = -1
            
            if HEAD == last:
                while table[HEAD] == -1:
                    HEAD -= 1
                last = HEAD
            else:
                while table[HEAD] == -1:
                    HEAD += 1
            
        elif command[0] == "Z":
            tmp = stack.pop()
            table[tmp] = tmp
            if tmp > last:
                last = tmp
        # print(HEAD, table, last)
    
    for i in range(n):
        if table[i] == -1:
            answer += "X"
        else:
            answer += "O"
        
    return answer

# class Node:
#     def __init__(self, data):
#         self.value = data
#         self.prev = None
#         self.next = None
        
#     def __str__(self):
#         return str(self.value)