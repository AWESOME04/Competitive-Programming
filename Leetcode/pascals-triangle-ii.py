class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Base case
        # if rowIndex == 0:
        #     return [1]

        # # Using Recursion
        # prevIndex = self.getRow(rowIndex-1)
        # res = [1] * (len(prevIndex)+1)

        # for i in range(1, len(res)-1):
        #     res[i] = prevIndex[i-1] + prevIndex[i]

        # return res

        # Time Complexity: O(n^2)
        # Space Complexity: O(n)


        # Optimized Approach
        row = [1] 

        for i in range(1, rowIndex + 1):
            next_row = [1]  
            for j in range(1, i):
                next_element = row[j - 1] + row[j]  
                next_row.append(next_element)
            next_row.append(1)  
            row = next_row  

        return row

        # Time Complexity: O(rowIndex^2)
        # Space complexity: O(rowIndex)
