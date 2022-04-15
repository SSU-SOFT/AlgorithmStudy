import sys

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word=True

    def search(self, word:str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.word

    def startsWith(self, prefix:str):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
        
def sol():
    N, M = map(int, sys.stdin.readline().strip().split(" "))
    answer = 0
    S = Trie()
    for _ in range(N):
        string = sys.stdin.readline().strip()
        S.insert(string)

    for _ in range(M):
        string = sys.stdin.readline().strip()
        if S.search(string):
            answer += 1

    return answer
print(sol())