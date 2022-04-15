def solution(participant, completion):
    answer = ''
    part = {}
    for p in participant:
        if not p in part:
            part[p] = 1
        else:
            part[p] += 1
    
    for c in completion:
        if c in part:
            part[c] -= 1

    for k, v in part.items():
        if v == 1:
            answer = k
    
    return answer