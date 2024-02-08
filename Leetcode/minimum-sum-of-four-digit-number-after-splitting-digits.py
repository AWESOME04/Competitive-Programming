class Solution:
    def minimumSum(self, num: int) -> int:
        res = sorted(str(num))
        return (int(res[0] + res[2]) + int(res[1] + res[3]))
