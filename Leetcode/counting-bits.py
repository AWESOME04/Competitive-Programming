class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        sum = 0

        for i in range(n+1):
            sum = bin(i).count('1')
            ans.append(sum)
        return ans
