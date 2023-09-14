class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n - 1

        while l<=r:
            m = l + (r-l) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1

        if l == n:
            return letters[0]
        else:
            return letters[l]
            
