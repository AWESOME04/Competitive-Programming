class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        res = list(s)
        l, r = 0, 1
        
        while r < len(res):
            if l >= 0 and (res[l].islower() and res[r].isupper() and res[l].upper() == res[r]) or (res[l].isupper() and res[r].islower() and res[r].upper() == res[l]):
                res.pop(l)
                res.pop(r-1)
                l, r = max(0, l-1), max(1, l)
            else:
                l += 1
                r += 1
        
        return "".join(res)
