import itertools
def solution(numbers):
    answer = 0
    num = set() 
    # Create Permutaion 
    for r in range(1, len(numbers)+1):
        for item in list(itertools.permutations(list(numbers), r)):
            num.add(int(''.join(item)))
    # Count Prime Number
    for n in num:
        if cntPrime(n):
            answer += 1
    return answer
def cntPrime(n):
    result = True
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if i < n and n%i == 0:
                return False
    return result