class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # n = len(gain)
        # prefix = [0] * (n+1)
        # for i in range(len(gain)):
        #     prefix[i+1] = prefix[i] + gain[i]
        
        # return max(prefix)

        maxx = 0
        res = 0
        for val in gain:
            res += val
            maxx = max(maxx, res)
        return maxx
        
