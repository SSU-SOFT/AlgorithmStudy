import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    # print(num, arr)
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)
    return 1

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)