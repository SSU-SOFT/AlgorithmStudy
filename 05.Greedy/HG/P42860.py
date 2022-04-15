def solution(name):
    answer = 0
    data = []
    visited = []
    for el in name:
        tmp = ord(el) - ord('A')
        if tmp > 13:
            tmp = 26 - tmp
        data.append(tmp)
        if tmp > 0:
            visited.append(False)
        else:
            visited.append(True)
    answer += sum(data)

    idx = 0
    tmp = 0
    print(data)
    while False in visited:
        visited[idx] = True
        data[idx] = 0
        print(data[idx+1:]+data[:idx])
        tmp = visited[idx+1:]+visited[:idx]
        # print(tmp)
        # print(tmp[::-1])
        li = 0; ri = 0
        # find li, ri
        for i, el in enumerate(tmp):
            if not el:
                ri = i+1
                break
        for i, el in enumerate(tmp[::-1]):
            if not el:
                li = i+1
                break

        # print("li, ri")
        # print(li, ri)

        if li < ri: # mv to left
            idx -= 1
            if idx < 0:
                idx = len(name)-1
        else: # mv to right
            idx += 1
            if idx >= len(name):
                idx = 0
        # print(idx)
        answer += 1
    return answer-1