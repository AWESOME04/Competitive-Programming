class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = int(m - 1)
        j = int(n - 1)
        k = int(m + n - 1)
        
        while (k >= 0):
            if i>=0 and j>=0:
                if(nums2[j] > nums1[i]):
                    nums1[k] = nums2[j]
                    k -= 1
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    k -= 1
                    i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                break
