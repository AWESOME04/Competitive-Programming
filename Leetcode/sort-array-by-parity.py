class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         res.append(nums[i])
        #     else:
        #         continue
        
        # for i in range(len(nums)):
        #     if nums[i] % 2 != 0:
        #         res.append(nums[i])
        
        # return res

        # Optimal Two Pointer Solution
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return nums
