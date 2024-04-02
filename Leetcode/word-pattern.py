class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res = s.split()

        return len(set(pattern)) == len(set(res)) == len(set(zip_longest(pattern, res)))
