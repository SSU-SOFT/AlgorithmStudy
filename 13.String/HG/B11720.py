import sys
input = sys.stdin.readline

N = int(input())
print(sum([int(ch) for ch in input().strip()]))