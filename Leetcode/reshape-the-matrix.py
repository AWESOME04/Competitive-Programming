class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat) 
        n = len(mat[0])  
        
        if m * n != r * c:
            return mat
        
        flattened = [num for row in mat for num in row]
        
        reshaped = []
        index = 0
        
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flattened[index])
                index += 1
            reshaped.append(row)
        
        return reshaped
