class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        nums = list(map(str, range(1, n+1)))
        fact = math.factorial(len(nums)-1)
        k -= 1

        while k:
            i, k = divmod(k, fact)
            ans += nums.pop(i)
            fact //= len(nums)
        ans += "".join(nums)
        return ans
