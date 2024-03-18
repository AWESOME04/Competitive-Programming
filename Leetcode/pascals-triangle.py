class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        triangle = self.generate(numRows - 1)
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])
        
        new_row.append(1)
        triangle.append(new_row)

        return triangle
        
