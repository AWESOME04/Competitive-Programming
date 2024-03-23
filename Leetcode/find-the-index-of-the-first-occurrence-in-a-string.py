class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack: - O(n^2)
        #     return haystack.index(needle)
        # return -1

        # n, m = len(needle), len(haystack) - O(n*m)
        
        # for i in range(m-n+1):
        #     if haystack[i:i+n] == needle:
        #         return i
        # return -1

        # Using Knuth-Morris-Pratt(KMP) Algo - O(n+m)
        if needle == "":
            return 0
        
        lps = [0] * len(needle)
        prevLPS, i = 0, 1

        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0 # pointer for haystack
        j = 0 # pointer for needke
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1
