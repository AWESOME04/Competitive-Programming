class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)

            if max1 > max2:
                smash = max1 - max2
            elif max1 < max2:
                smash = max2 - max1
            else:
                smash = 0

            stones.append(smash)
        
        if len(stones) == 1:
            return stones[0]
        
        if not stones:
            return 0

