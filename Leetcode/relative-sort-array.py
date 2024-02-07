class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in range(0, len(arr2)):
            while arr2[i] in arr1:
                res.append(arr2[i])
                arr1.remove(arr2[i])
        
        arr1.sort()
        res.extend(arr1)
        return res
