K = int(input())
buildings = input().split(" ")
tree = []

while K > 0:
    result = buildings[::2]
    buildings = list(map(lambda x : x[1], filter(lambda x : x[0]%2==1, enumerate(buildings))))
    tree.append(result)
    K-=1

for level in tree[::-1]:
    print(' '.join(level))