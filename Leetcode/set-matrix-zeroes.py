class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

    # row is the len of the matrix.i.e: len(matrix)
    # column is the len of the first matrix. i.e len(matrix[0])

        storage = []
        for index_of_row in range(len(matrix)):
            for index_of_column in range(len(matrix[0])):
                if matrix[index_of_row][index_of_column] == 0:
                    storage.append((index_of_row, index_of_column))
        
        for item in storage:
            index_of_row, index_of_column = item

            # Setting the entire row to zero
            matrix[index_of_row] = [0] * len(matrix[0])

            # Setting the entire column to zero
            for rows in range(len(matrix)):
                matrix[rows][index_of_column] = 0

        return matrix
