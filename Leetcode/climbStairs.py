class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        if n <= 3:
            return n
        else:
            for i in range(1, n):
                c = a + b
                a = b
                b = c
            return b

        # Time Complexity: 
        # Space Complexity: 
