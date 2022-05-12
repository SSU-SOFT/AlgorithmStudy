def pprint(arr):
    for line in arr[1:]:
        print(line[1:])

def dfs(cur, intensity, summits, minValue):
    result = [[float('inf'), float('inf')]]
    st = [(cur, intensity)]
    # print("start", cur, intensity, minValue)

    while st:
        cur, intensity = st.pop()
        # print(cur, intensity)
        # print(visited)
        if cur in summits:
            # print("summit", cur, intensity)
            if intensity <= minValue:
                minValue = intensity
                result.append([cur, intensity])
            continue
        
        if visited[cur]:
            continue
        visited[cur] = True

        for nxt, w in enumerate(graph[cur]):
            if w == 0:
                continue
            if not visited[nxt]:
                if intensity == float('inf'):
                    st.append((nxt, w))
                else:
                    if w <= minValue:
                        if w <= intensity:
                            st.append((nxt, intensity))
                        else:
                            st.append((nxt, w))
    # print(result)
    return sorted(result, key=lambda x: (x[1], x[0]))[0]

def solution(n, paths, gates, summits):
    answer = []
    global graph
    graph = [[0] * (n+1) for _ in range(n+1)]
    global visited
    visited = [False] * (n+1)

    for i, j, w in paths:
        graph[i][j] = w
        graph[j][i] = w

    result = []
    minValue = float('inf')

    for gate in gates:
        visited = [False] * (n+1)
        result = dfs(gate, float('inf'), summits, minValue)
        if result[1] < minValue:
            answer = result
            minValue = result[1]
        # print("answer============")
        # print(result)

    return answer