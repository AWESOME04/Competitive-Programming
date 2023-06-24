class Solution:
   def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        count = 0
        for item in matrix:
            if target in item:
                return True
            else:
                continue
        return False

