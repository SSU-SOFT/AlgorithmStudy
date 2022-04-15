import sys
input = sys.stdin.readline

def isPalindrome(string, l, r, UseDelete):
    IsPseudoPalindrome = True
    while 0 <= l and r < len(string) and l <= r:
        if string[l] == string[r]:
            l += 1
            r -= 1
        else:
            if not UseDelete:
                return isPalindrome(string, l+1, r, True) | isPalindrome(string, l, r-1, True)
            else:
                return False
    return IsPseudoPalindrome

for _ in range(int(input())):
    string = input().strip()
    # print(string,"=================")
    # Palindrome
    if string == string[::-1]:
        print(0)
        continue

    # Is Psuedo Palindrome?
    # Devide half string
    result = isPalindrome(string, 0, len(string)-1, False)
    if result:
        print(1)
    else:
        print(2)