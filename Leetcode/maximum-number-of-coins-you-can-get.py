class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        
        if len(piles) == 3:
            return piles[1]

        for i in range(len(piles)//3):
            sum += piles[-i*2-2]
        return sum
        
