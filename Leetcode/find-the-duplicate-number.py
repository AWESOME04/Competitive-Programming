class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Uses O(n) space for the count_nums array so isn't ideal

        # n = len(nums)
        # count_nums = Counter(nums)

        # for num, count in count_nums.items():
        #     if count > 1:
        #         return num


        # Uses O(n) space for the visited set so isn't ideal

        # n = len(nums)
        # visited = set()
        # visited.add(nums[0])

        # for i in range(1, n):
        #     if nums[i] not in visited:
        #         visited.add(nums[i])
        #     else:
        #         return nums[i]

        # Using Floyd's Cycle Detection (Linked list cycle detection)
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        # Second Phase
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
    
