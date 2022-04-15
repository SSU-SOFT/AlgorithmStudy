N, K = input().split(" ")
answer = []
q = [i for i in range(1, int(N)+1)]
# print(q)
idx = 0
while q:
    idx = (idx + int(K)-1) % len(q)
#     print(idx, q)
    answer.append(str(q.pop(idx)))
print("<"+", ".join(answer)+">")