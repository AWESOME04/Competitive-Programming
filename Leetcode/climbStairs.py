class Solution:
        def climbStairs(self, n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2

            n2 = 2
            n3 = 3 

            for i in range(n-3):
                n3, n2 = n3+n2, n3

            return n3
        

        # Time Complexity: O(N)
        # Space Complexity: O(1)
