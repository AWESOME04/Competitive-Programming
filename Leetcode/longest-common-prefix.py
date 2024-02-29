# Trie Implementation
class TrieNode:
        def __init__(self):
            self.children = {}
            self.occurrence = 1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        n = len(strs)
        prefix = ""

        for s in strs:
            cur = root
            for i in s:
                if i not in cur.children:
                    cur.children[i] = TrieNode()
                else:
                    cur.occurrence += 1
                
                if cur.occurrence == n:
                    prefix += i
                cur = cur.children[i]
        
        return prefix    

# class Solution:
#   def longestCommonPrefix(self, strs: List[str]) -> str:
#     if not strs:
#       return ''

#     for i in range(len(strs[0])):
#       for j in range(1, len(strs)):
#         if i == len(strs[j]) or strs[j][i] != strs[0][i]:
#           return strs[0][:i]

#     return strs[0]
