class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                # O(n) solution
                # indices = []
                # indices2 = []
                # for (index, item) in enumerate(nums):
                #     if item == target:
                #         indices.append(index)
                # for num in indices:
                #     if len(indices) == 1:
                #         indices.append(num)
                #     elif len(indices) >= 3:
                #         indices2.append(indices[0])
                #         indices2.append(indices[-1])
                #         return indices2
                # return indices    

                # O(logN) solution 
                first = bisect.bisect_left(nums, target)
                last = bisect.bisect_right(nums, target)
                return [first, last-1]

        return [-1, -1]
