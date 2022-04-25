def solution(n, k, cmd):
    answer = ['O'] * n
    HEAD = None
    root = Node(0)
    cur = root
    for i in range(1, n):
        cur.next = Node(i)
        cur.next.prev = cur
        cur = cur.next
        if i == k:
            HEAD = cur
            
    stack = []
    
    for command in cmd:
        # print(command)
        if command[0] == "U":
            C, X = command.split()
            for _ in range(int(X)):
                HEAD = HEAD.prev
            # print("current : ", HEAD)
        elif command[0] == "D":
            C, X = command.split()
            for _ in range(int(X)):
                HEAD = HEAD.next
            # print("current : ", HEAD)
        elif command[0] == "C":
            stack.append(HEAD)
            tmp = HEAD
            #Connect prev to next
            if not HEAD.prev == None:
                HEAD.prev.next = HEAD.next
            if not HEAD.next == None:
                HEAD.next.prev = HEAD.prev
            
            #Change HEAD pointer
            if HEAD.next == None:
                HEAD = HEAD.prev
            else:
                HEAD = HEAD.next
            
            # print("current : ", HEAD)
        elif command[0] == "Z":
            # print("Undo :", stack[-1])
            node = stack.pop()
            
            if not node.prev == None:
                node.prev.next = node
            if not node.next == None:
                node.next.prev = node
            # print("current : ", HEAD)
        
        # cur = root
        # while cur != None:
        #     print(cur.value, end=" ")
        #     cur = cur.next
        
        # print(stack)
        
    for node in stack:
        answer[node.value] = "X"
    
    return "".join(answer)

class Node:
    def __init__(self, data):
        self.value = data
        self.prev = None
        self.next = None
        
    def __str__(self):
        return str(self.value)
