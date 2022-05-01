# 완전 탐색(BruteForce)
완전 탐색(BruteForce)은 컴퓨터의 빠른 계산 능력을 이용해 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법을 의미한다. 가능한 방법을 전부 만들어 보는 알고리즘을 뜻하며, 직관적이고 이해하기 쉬워 문제의 정확한 결과값을 얻어낼 수 있는 가장 확실하며 기초적인 방법이다. 

## 완전탐색 기법을 활용하는 방법
1) 해결하고자 하는 문제의 가능한 경우의 수를 대략적으로 계산한다.
2) 가능한 모든 방법을 다 고려한다.
3) 실제 답을 구할 수 있는지 적용한다.

## 완전탐색 기법
1. 반복 / 조건문을 활용해 모두 테스트 하는 방법
2. 순열(Permutation) - n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
3. 재귀 호출
4. 비트마스크 - 2진수 표현 기법을 활용하는 방법
5. BFS, DFS를 활용하는 방법

### 순열과 조합
- 순열(Permutation) : n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
- 조합(Combination) : n개의 원소 중 r개의 원소를 순서에 상관없이 선택하는 방법

__python에서의 순열,조합 사용방법__
library itertools
- 소스코드
```
def permutations(iterable, r=None):
    result = []
    n = len(seq)
    r = number if not number is None else len(seq)
    if r == 0:
        return [result]

    for i in range(n):
        fix = seq[i]
        tmp = seq[i+1:] + seq[:i]
        for arr in my_permutations(tmp, r-1):
            result.append((fix, *arr))
    return result
```
    
```
def combinations(iterable, r):
    result = []
    n = len(seq)
    r = number if not number is None else len(seq)
    if r == 0:
        return [result]

    for i in range(n):
        fix = seq[i]
        tmp = seq[i+1:]
        for arr in my_combinations(tmp, r-1):
            result.append((fix, *arr))
    return result
```
    
```
import itertools as it
arr = [1,2,3,4,5]
string = 'ABCD'

it.permutations(arr)
it.permutations(string, 2)

it.combinations(arr, 3)
it.combinations(string, 2)
```