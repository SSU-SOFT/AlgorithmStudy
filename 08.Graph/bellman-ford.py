def bellman_ford(graph, start):
    distance, predecessor = dict(), dict()  # 거리 값, 각 정점의 이전 정점을 저장할 딕셔너리
    # 거리 값을 모두 무한대로 초기화 / 이전 정점은 None으로 초기화
    for node in graph:  
        distance[node], predecessor[node] = float('inf'), None
    distance[start] = 0  # 시작 정점 거리는 0

    # 간선 개수(V-1)만큼 반복
    for _ in range(len(graph) - 1):
        print(_)
        for node in graph:
            print(node, distance)
            for neighbour in graph[node]:  # 각 정점마다 모든 인접 정점들을 탐색
                # (기존 인접 정점까지의 거리 > 기존 현재 정점까지 거리 + 현재 정점부터 인접 정점까지 거리)인 경우 갱신
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]
                    predecessor[neighbour] = node

                print(neighbour, predecessor)
            print(node, distance)
            print("=======================")

    # 음수 사이클 존재 여부 검사 : V-1번 반복 이후에도 갱신할 거리 값이 존재한다면 음수 사이클 존재
    for node in graph:
        for neighbour in graph[node]:
            if distance[neighbour] > distance[node] + graph[node][neighbour]:
                return -1, "그래프에 음수 사이클이 존재합니다."

    return distance, predecessor
    
    
# 음수 사이클이 존재하지 않는 그래프
graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3}
}

# 그래프 정보와 시작 정점을 넘김
distance, predecessor = bellman_ford(graph, start='A')

print(distance)
print(predecessor)

print("===================")
# 음수 사이클이 존재하는 그래프
graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {'A': -5},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3}
}


distance, predecessor = bellman_ford(graph, start='A')

print(distance)
print(predecessor)