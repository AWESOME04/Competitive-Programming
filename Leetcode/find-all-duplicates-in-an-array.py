class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = []
        # count_nums = Counter(nums)


        # for num, count in count_nums.items():
        #     if count > 1:
        #         res.append(num)
        # return res


        # Cyclic Sort
        n = len(nums)
        i = 0
        res = []

        while i < n:
            correct_position = nums[i] - 1
            if nums[i] != nums[correct_position]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res
