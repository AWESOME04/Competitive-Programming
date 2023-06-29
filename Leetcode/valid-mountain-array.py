class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        peak_index = arr.index(max(arr))
        
        if peak_index == 0 or peak_index == len(arr) - 1:
            return False
        
        for i in range(peak_index):
            if arr[i] >= arr[i + 1]:
                return False
        
        for j in range(peak_index, len(arr) - 1):
            if arr[j] <= arr[j + 1]:
                return False
        
        return True
