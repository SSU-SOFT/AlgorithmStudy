from collections import defaultdict
def dfs(start, data):
    result = set()
    st = [start]
    visited = []
    
    while st:
        cur = st.pop()
        visited.append(cur)
        
        for nxt in data[cur]:
            if nxt not in visited:
                result.add(nxt)
                st.append(nxt)
    
    return result
    

def solution(n, results):
    answer = 0
    global win, lose
    win = defaultdict(set)   
    lose = defaultdict(set)
    
    for a, b in results:
        win[a].add(b)
        lose[b].add(a)
        
    for i in range(1, n+1):
        if len(dfs(i, win)) + len(dfs(i, lose)) == n-1:
            answer += 1    
    
    return answer