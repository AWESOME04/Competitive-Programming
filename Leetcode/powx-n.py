class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n
        # return pow(x, n)

        # Using Recursion
        if n == 0:
            return 1
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n
        
        half_pow = Solution.myPow(self,x, n // 2)
        
        if n % 2 == 0:
            return half_pow * half_pow
        else:
            return half_pow * half_pow * x
