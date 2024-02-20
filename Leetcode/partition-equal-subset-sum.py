class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            next_dp = set()
            for t in dp:
                next_dp.add(t + nums[i])
                next_dp.add(t)
            dp = next_dp
        return True if target in dp else False        
