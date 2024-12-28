class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        return len(s.split(" ")[-1])

        # TC: O(N) - Traversal
        # SC: O(k) - Temp storage of the last word
        
