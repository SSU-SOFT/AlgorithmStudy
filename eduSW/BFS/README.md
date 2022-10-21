모든 경우의 수 확인
Greedy한 논리의 사용 불가.

`1원, 4원, 6원 동전을 이용하여 8원을 최소 갯수의 동전으로 만들기`

- 장점 : 반례를 생각할 필요가 없는 매우 단순한 문제 해결 방법.
- 단점 : 모든 경우의 수를 따져보기 위해 많은 연산량이 필요함.

 ## BFS, DFS
 - Tree나 Graph에서 모든 노드를 탐색하기 위한 탐색 알고리즘 중 하나.
 - 모든 경우의 수를 탐색하는 방법으로도 사용됨.

1. 노드 - 상태, root 노드 - 초기 상태, leaf 노드 - 목적 상태
2. 탐색 과정에서 자식 노드로의 이동의 의미.
3. Root Node에서 LeafNode까지의 경로 하나의 탐색
4. Tree 전체 노드의 탐색 의미.

# BFS (Breadth First Search) 탐색 전략
- 초기 상태에서부터 탐색 시작.
- FIFO Queue를 사용.

### BFS 기본 코드 형태
```
while(!Queue.Empty()) {
    Dequeue(current state);
    state calculate -> next state;
    Enqueue(next state);
}
```

### 중요 특징
1. 모든 경우의 수 동시 다발적으로 진행
2. FIFO Queue 이용하여 구현할 경우 모든 경우의 수가 평등하게 발전.

BFS/DFS 구현시 결정사항
- 상태 / 상태 발전 정의
- 경우의 수 가지치기 조건 계획.
-> BFS/DFS의 많은 연산량을 고려. (특히 BFS로 해결하는 문제의 경우 연산량이 매우 큼)
※ 최단 거리
- 가중치가 같은 경우 : 중복 방문x, 도착점에 도달하면 끝.
- 가중치가 다른 경우 : 중복 방문o, Queue가 Empty할때까지 iterate.

# DFS (Depth First Search) 탐색 전략
- 