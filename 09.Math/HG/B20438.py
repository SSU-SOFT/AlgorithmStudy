import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
students = [0] * (N+3)
sleep = list(map(int, input().split()))
Attendance = list(map(int, input().split()))

for num in sleep:
    students[num] = -1

for num in Attendance:
    if students[num] != -1:
        for i in range(1, (N+2)//num+1):
            if students[i*num] != -1:
                students[i*num] = 1
# print(students)
sumarr = [0] * (N+3)
for i in range(3, len(students)):
    sumarr[i] = sumarr[i-1]
    if students[i] != -1:
        sumarr[i] += students[i]

# print(sumarr)
for _ in range(M):
    S, E = map(int, input().split())
    answer = (E-S+1) - (sumarr[E] - sumarr[S-1])
    
    print(answer)

