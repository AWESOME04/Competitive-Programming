class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # ans1 = set()
        # ans2 = set()
        
        # for num in nums1:
        #     if num not in nums2:
        #         ans1.add(num)

        # for num in nums2:
        #     if num not in nums1:
        #         ans2.add(num)
            
        # return [ans1, ans2]

        first = list(set(nums1) - set(nums2))
        second = list(set(nums2) - set(nums1))
        
        return [first, second]
