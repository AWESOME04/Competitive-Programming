class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)

        prev = 0
        for i in range(n):
            prev = min(prev + 1, arr[i])
        return prev
        
        # TC: O(nlogn)
        # SC: O(1)
