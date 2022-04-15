import sys
input = sys.stdin.readline
global n
n = int(input())

S = 1
while S < n:
    S *= 2

global tree, arr
tree = [0] * (S*2)
arr = [0] + list(map(int, input().strip().split()))
print(arr)
def makeTree(node, l, r):
    if l == r:
        if l <= n:
            tree[node]=arr[l]
            return tree[node]
        else:
            tree[node] = -float('inf')
            return tree[node]

    mid = (l+r)//2
    tree[node] = makeTree(node*2, l, mid)
    tree[node] += makeTree(node*2+1, mid+1, r)
    
    return tree[node]

def query(node, left, right, qleft, qright):
    if qright < left or right < qleft:
        return 0
    elif qleft <= left and right <=qright:
        return tree[node]
    else:
        mid = (left+right) // 2
        return query(node*2, left, mid, qleft, qright) + query(node*2+1, mid+1, right, qleft, qright)

makeTree(1,1,S)
print(tree)
maxValue = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        maxValue = max(maxValue, query(1, 1, S, i, j))

print(maxValue)