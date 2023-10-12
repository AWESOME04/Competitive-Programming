from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        results = []
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram[sorted_s].append(s)

        for val in anagram.values():
            results.append(val)

        return results
