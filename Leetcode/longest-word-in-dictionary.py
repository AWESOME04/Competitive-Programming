class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.val = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
        cur.val = word

    def bfs(self):
        ans = [self.root]
        res = ""
        while ans:
            cur = ans.pop(0)
            for child in cur.children.values():
                if child.is_end:
                    ans.append(child)
                    if len(child.val) > len(res):
                        res = child.val
        return res

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie.bfs()
        
