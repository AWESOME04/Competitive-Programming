class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []

        for k, v in count2.items():
            if k in count1:
                res.extend([k] * min(v, count1[k]))
        return res
