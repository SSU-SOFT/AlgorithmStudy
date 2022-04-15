N, M = map(int, input().split())

indegree = [0] * (N+1)
students = {}

for _ in range(M):
    A, B = map(int, input().split())
    if B in students:
        students[B].append(A)
    else:
        students[B] = [A]
    
    indegree[B] += 1


print(students)
print(indegree)