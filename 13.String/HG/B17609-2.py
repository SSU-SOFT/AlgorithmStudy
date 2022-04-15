import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().strip()
    IsPseudoPalindrome = False
    # 회문
    if string == string[::-1]:
        print(0)
        continue

    # palindrome search
    for i in range(0, len(string)):
        tmp = string[0:i] + string[i+1:len(string)] # O(n)
        if tmp == tmp[::-1]:                        # O(n)
            IsPseudoPalindrome = True
            break
    # O(n^2)


    if IsPseudoPalindrome:
        print(1)
    else:
        print(2)
    