class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

# Alternative Solution

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         res = []
#         l, r = 0, 0
#         while l < len(word1) and r < len(word2):
#             res.append(word1[l])
#             res.append(word2[r])
#             l += 1
#             r += 1
            
#         if l < len(word1):
#             res.extend(word1[l:])
#         elif r < len(word2):
#             res.extend(word2[r:])

#         return "".join(res)
