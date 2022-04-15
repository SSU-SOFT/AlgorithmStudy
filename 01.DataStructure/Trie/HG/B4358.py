import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.cnt = 0
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
        node.cnt += 1

    def search(self, word:str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.cnt
            
    def pprint(self, node, string):
        global l
        if node.cnt > 0:
            print(string, '{:.4f}'.format(node.cnt / l * 100, 4))
        
        for ch in sorted(node.children.keys()):
            self.pprint(node.children[ch], string + ch)
            pass

global l
l = 0
tree = Trie()
while True:
    string = input().strip()
    if string == '':
        break
    l += 1
    tree.insert(string)

tree.pprint(tree.root, '')
