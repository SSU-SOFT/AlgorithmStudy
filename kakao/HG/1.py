from collections import defaultdict
def solution(survey, choices):
    answer = ''
    result = defaultdict(int)
    # positive : R, C, J ,A
    # negative : T, F, M, N
    score = [0, 3, 2, 1, 0, 1, 2, 3]

    for i in range(len(survey)):
        pos = survey[i][0]
        neg = survey[i][1]
        #동의인지 비동의인지 확인
        if choices[i] // 4 < 1: # 동의인 경우
            result[pos] += score[choices[i]]
        else:
            result[neg] += score[choices[i]]

    if result['R'] >= result['T']:
        answer += 'R'
    else:
        answer += 'T'

    if result['C'] >= result['F']:
        answer += 'C'
    else:
        answer += 'F'

    if result['J'] >= result['M']:
        answer += 'J'
    else:
        answer += 'M'

    if result['A'] >= result['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer