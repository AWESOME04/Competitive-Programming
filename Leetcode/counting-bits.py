class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        bit = 0

        for i in range(n+1):
            bit = bin(i).count('1')
            ans.append(bit)
        return ans
