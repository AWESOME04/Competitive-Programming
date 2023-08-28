class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Using Two Pointers

        res = 0

        # Initilizing two pointers
        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[r], height[l])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

        # Time Complexity: O(n)
        # Space Complexity: O(1)
