class Node:
    def __init__(self):
        self.cnt_prf = 0
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            node.cnt_prf += 1

    def get_sum_prf(self, word):
        node = self.root
        cnt = 0
        for c in word:
            if c not in node.children:
                break
            node = node.children[c]
            cnt += node.cnt_prf

        return cnt

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return [trie.get_sum_prf(word) for word in words]
        
