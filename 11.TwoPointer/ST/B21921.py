import sys
input = sys.stdin.readline
N, X = map(int, input().split())
visitor = list(map(int, input().split()))
max_visitor = 0
max_visitor_count = 0
for i in range(1, N):
    visitor[i] += visitor[i-1]

visitor.insert(0, 0)

for i in range(X, N+1):
    period_visitor = visitor[i] - visitor[i-X]
    if(max_visitor < period_visitor):
        max_visitor = period_visitor
        max_visitor_count = 1
    elif(max_visitor == period_visitor):
        max_visitor_count += 1

if(max_visitor == 0):
    print("SAD")
else:
    print(max_visitor)
    print(max_visitor_count)