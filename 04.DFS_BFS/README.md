## 깊이우선탐색, 너비우선탐색 (DFS / BFS)

### 깊이 우선 탐색 (DFS, Depth First Search)

한 경로로 탐색하다 특정 상황에서 최대한 깊숙하게 들어가서 확인 후 다시 돌아가 다른 경로로 탐색하는 방식.

BFS와의 큰 차이점은 DFS는 탐색을 한 뒤 이전의 정점으로 돌아온다는 것이다. 이것을 백트래킹이라고 한다.

그래프 알고리즘에서 기초가 되는 탐색 방식으로 반드시 숙지가 필요하다.

DFS 활용 : 백트래킹(경우의 수), 단절선 찾기, 단절점 찾기, 위상정렬, 사이클 찾기 등.

__DFS 순서__
> 1. 체크 인
> 2. 목적지에 도착했는가?
> 3. 연결된 곳을 순회
> 4. 갈 수 있는 가?
> 5. 간다.
> 6. 체크아웃, 돌아온 체크를 아웃.

- 재귀 용법
```
visited = []

def dfs(v):
    if isGoal:
        return
    visited[v] = True # visited.append(v)
    
    for i in G[v]:
        if not visited[v]:
            DFS(i)

    visited[v] = False
```
- 스택 이용
```
def dfs(v):
    st = []
    st.append(v)

    while st:
        cur = st.pop()
        if isGoal:
            break
        visited[cur] = True
        for v in G[cur]:
            if not visited[v]:
                st.append(v)
```
### 너비 우선 탐색 (BFS, Breath First Search)

시작 노드에서 시작하여 인접한 노드를 먼저 탐색하는 방식. 트리구조에서는 계층 순회를 시작하고 각 계층의 모든 노드를 탐색한 뒤 그 아래 계층으로 넘어간다 . 일반적으로 Queue 자료구조를 이용하여 구현. 
        
BFS 활용 : 최단 경로 찾기, 위상정렬 등.
* BFS로 최단 경로 문제를 해결 가능한 것은 가중치가 1일때 만이다. 1이 아니라면 다익스트라 혹은 벨만 포드 알고리즘을 같이 응용하여 사용해야한다.

__BFS 순서__
> 1. 큐에서 꺼내옴
> 2. 목적지에 도달했는가?
> 3. 연결된 곳을 순회
> 4. 갈 수 있는가?
> 5. 체크인 & 큐에 넣음(간다)
> 6. 체크아웃 (일반적으로 사용 X) 
> -> 한번 방문한 곳은 다시 들어가지 않기 때문에 체크아웃 하지 않아도 됨.

```
from collections import deque
# deque를 사용하는 이유는 list.pop(0)를 하게되면 O(n)의 시간복잡도를 갖는다.

def bfs(G, s):
    q = deque()

    while q:
        cur = q.popleft()
        if isGoal:
            break
        for v in G[cur]:
            if canGo:
                visited[v] = True
                q.append(v)
```