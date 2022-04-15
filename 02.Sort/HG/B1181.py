import sys

N = int(input())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())
    
for word in sorted(set(words), key= lambda x : (len(x), x)):
    print(word)