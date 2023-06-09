class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl= list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        n = len(sl)
        for i in range(n):
            tl.remove(sl[i])
        return tl[0]
