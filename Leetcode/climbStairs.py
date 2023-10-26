class Solution:
    def climbStairs(self, n: int) -> int:
        n1 , n2 = 0, 1

        for i in range(n):            
            n1, n2 = n2, n1+n2
        return n2
        

        # Time Complexity: O(N)
        # Space Complexity: O(1)
