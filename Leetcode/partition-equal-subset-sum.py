class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom Up Approach
        # if sum(nums) % 2:
        #     return False

        # dp = set()
        # dp.add(0)
        # target = sum(nums) // 2

        # for i in range(len(nums)-1, -1, -1):
        #     next_dp = set()
        #     for t in dp:
        #         next_dp.add(t + nums[i])
        #         next_dp.add(t)
        #     dp = next_dp
        # return True if target in dp else False

        # Top Down Approach
        n = len(nums)
        memo = defaultdict(int)

        def dp(i, target_sum):
            if i >= n or target_sum <= 0:
                return target_sum == 0
            
            state = (i, target_sum)
            if state not in memo:
                memo[state] = dp(i+1, target_sum-nums[i]) or dp(i+1, target_sum)
            return memo[state]
        
        return sum(nums) % 2 == 0 and dp(0, sum(nums) // 2)
