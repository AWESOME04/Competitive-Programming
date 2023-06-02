class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(1.0*s.count(letter)/len(s)*100)
