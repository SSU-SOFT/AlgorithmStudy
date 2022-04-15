## 탐욕 알고리즘 (Greedy)
- 답을 하나씩 고르는데, 미리 정한 기준에 따라서 매번 '가장 좋아 보이는' 답을 선택한다. 
- 로컬 최적해를 찾는 탐욕스런 방법으로는 문제를 해결 할 수 없다. 그러나 합리적인 시간 내에 최적에 가까운 답을 찾을 수 있다는 점에서 매우 유용한 알고리즘이기도 하다.
- 그리디 알고리즘이 잘 사용되는 문제는 탐욕선택속성(Greedy Choice Property)을 갖고 있는 최적 부분 구조인 문제들이다. 
- 탐욕선택속성은 `앞의 선택이 이후 선택에 영향을 주지 않는 것`을 말한다. 즉, 선택을 다시 고려하지 않는다.
- 최적부분구조란 문제의 `최적 해결 방법이 부분 문제에 대한 최적 해결 방법으로 구성되는 경우`를 말한다.

## 예시 
### 1. 배낭문제
`배낭에 담을 수 있는 무게의 최댓값(15kg)이 정해져 있고 각각 짐의 가치($)와 무게(kg)가 있는 짐들을 배낭에 넣을 때 가치의 합이 최대가 되도록, $의 가치가 최대가 되도록 짐을 고르는 방법을 찾는 문제`
- [짐 챙기는 숌 문제링크](https://www.acmicpc.net/problem/1817)

### 2. 거스름돈 문제
`동전이 10월 50원 100원처럼 증가하면서 이전 액수의 배수 이상이 되면 그리디 알고리즘으로 풀 수 있다. 160원을 거슬러 준다면 10원짜리 16개보다는 100원짜리 하나, 50원짜리 하나, 10원짜리 하나로 가장 적은 동전 개수로 거슬러 줄 수 있는 방법이다. `
- [거스름돈 문제링크](https://www.acmicpc.net/problem/14916)

-> `그러나 80원짜리 동전이 있다고 치면, 80원 2개가 최적이지만 그리디 알고리즘으로는 100원부터 선정하게 될 것이며, 이런 경우 DP로 풀어야 한다.`

### 3. 가장 큰 합 (실패사례)
```
    7
  3  12
99 8 5 6
```

`트리 노드를 계속 더해가다가 마지막에 가장 큰 합이 되는 경로를 찾는 문제이다. 7 -> 12 -> 6 으로 greedy하게 선택하면, 25에 불과하지만, 7 -> 3 -> 99는 109가 될 수 있기 때문에 이진트리를 정렬하지 않는이상 그리디 알고리즘으로 풀수 없다.`


### 4. 다익스트라 알고리즘
- `가중 그래프 G와 간선, 시작점 s가 주어졌을 때, 시작점으로부터 그래프의 임의의 정점까지 최단거리를 구해주는 알고리즘이다.`
- `음이 아닌 가중치를 갖는 무작위 유향 그래프에서의 단일소스 최단 경로 알고리즘 중 점근적으로 가장 빠른 알고리즘이다.`

### 알고리즘 방법
<image src="./image/Dijkstra_Animation.gif">

1. 모든 꼭짓점을 미방문 상태로 표시한다. 미방문 집합이라는 모든 미방문 꼭짓점의 집합을 만든다.
2. 모든 꼭짓점에 시험적 거리 값을 부여한다: 초기점을 0으로, 다른 모든 꼭짓점을 무한대로 설정한다. 초기점을 현재 위치로 설정한다.
3. 현재 꼭짓점에서 미방문 인접 꼭짓점을 찾아 그 시험적 거리를 현재 꼭짓점에서 계산한다. 새로 계산한 시험적 거리를 현재 부여된 값과 비교해서 더 작은 값을 넣는다. 예를 들어, 현재 꼭짓점 A의 거리가 6이라고 표시되었고, 인접 꼭짓점 B로 연결되는 변의 길이가 2라고 한다면, A를 통한 B까지의 거리는 6 + 2 = 8이 된다. 이전의 B까지의 거리가 8보다 컸다면 8로 바꾸고, 그렇지 않다면 그대로 놔둔다.
4. 만약 현재 꼭짓점에 인접한 모든 미방문 꼭짓점까지의 거리를 계산했다면, 현재 꼭짓점을 방문한 것으로 표시하고 미방문 집합에서 제거한다. 방문한 꼭짓점은 이후에는 다시 방문하지 않는다.
5. 두 꼭짓점 사이의 경로를 찾는 경우: 도착점이 방문한 상태로 표시되면 멈추고 알고리듬을 종료한다.
6. 완전 순회 경로를 찾는 경우: 미방문 집합에 있는 꼭짓점들의 시험적 거리 중 최솟값이 무한대이면 이는 출발점과 미방문 집합 사이에 연결이 없는 경우이므로 멈추고 알고리즘을 종료한다.
7. 아니면 시험적 거리가 가장 작은 다음 미방문 꼭짓점을 새로운 "현재 위치"로 선택하고 3단계로 되돌아간다.

경로를 계획하고 있을 때, 사실은 위에서 했던 것처럼 도착점이 "방문"한 상태가 될 때까지 기다릴 필요가 없다: 도착점이 "미방문" 꼭짓점들 중 가장 시험적 거리가 작아지면 (그리고 다음 "현재 위치"로 선택될 수 있다면) 알고리즘을 종료할 수 있다.
---
1. 출발 노드와, 도착 노드를 설정
2. 알고 있는 모든 거리 값을 부여
3. 출발 노드부터 시작하여, 방문하지 않은 인접 노드를 방문, 거리를 계산한 다음, 현재 알고있는 거리보다 짧으면 해당 값으로 갱신한다.
4. 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드는 방문한 것이므로, 미방문 집합에서 제거한다.
5. 도착 노드가 미방문 노드 집합에서 벗어나면, 알고리즘을 종료한다.


### 의사 코드 (psuedo code)
```
function Dijkstra(Graph, source):
    dist[source] ← 0                           // 초기화

    create vertex set Q

    for each vertex v in Graph:
        if v ≠ source
            dist[v] ← INFINITY                 // 소스에서 v까지의 아직 모르는 길이
            prev[v] ← UNDEFINED                // v의 이전 노드

        Q.add_with_priority(v, dist[v])


    while Q is not empty:                      // 메인 루프
        u ← Q.extract_min()                    // 최고의 꼭짓점을 제거하고 반환한다
        for each neighbor v of u:              // Q에 여전히 남아 있는 v에 대해서만
            alt ← dist[u] + length(u, v)
            if alt < dist[v]
                dist[v] ← alt
                prev[v] ← u
                Q.decrease_priority(v, alt)

     return dist, prev
```
만약 source에서 target까지의 최단 경로만을 구하고 싶다면, 15번째 줄에 u = target을 추가해서 종료시킬 수 있다. 그리고 나서는 source에서 target까지의 최단 경로를 역방향 반복을 통해서 읽을 수 있다:

```
S ← empty sequence
u ← target
while prev[u] is defined:                // 스택 S로 최단 경로를 만든다
    insert u at the beginning of S         // 꼭짓점을 스택에 넣는다
    u ← prev[u]                           // target에서 source로 이동한다
insert u at the beginning of S             // source를 스택에 넣는다
```

### 코드구현 (Python)
```
#Input
# 6 9
# 1 2 7
# 1 3 9
# 1 6 14
# 2 3 10
# 2 4 15
# 3 4 11
# 3 6 2
# 4 5 6
# 5 6 9
import sys

N, M = map(int, input().split(" "))
G = [[0]* (N+1) for _ in range(N+1)]

def pprint(arr):
    for line in arr:
        print(line)

visited = [0 for _ in range(1+N)]

for _ in range(M):
    v1, v2, cost = map(int,sys.stdin.readline().split(" "))    
    G[v1][v2] = cost
    G[v2][v1] = cost

pprint(G)

import heapq as hq

def Dijkstra(Graph, source):    
    queue = []
    
    dist = [float('inf') for _ in range(1+N)]
    dist[source] = 0

    hq.heappush(queue, (dist[source], source))
    
    while queue:
        # print(queue)
        # print(dist)
        cur_dist, cur_dest = hq.heappop(queue)
        if dist[cur_dest] < cur_dist: # 기존에 있는 거리보다 긴 경우
            continue

        for i in range(1, N+1):
            new_dest = i
            new_dist = G[cur_dest][new_dest]
            if new_dist != 0:
                distance = cur_dist + new_dist
                if distance < dist[new_dest]:
                    dist[new_dest] = distance
                    hq.heappush(queue, (distance, new_dest))
        
    
    return dist

answer = Dijkstra(G, 1)
print(answer)
```
