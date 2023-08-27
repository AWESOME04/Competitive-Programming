class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                substr = s[:length]
                repeats = n // length
                if substr * repeats == s:
                    return True
        return False
