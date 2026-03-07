class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_zer = []
        row_zer = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col_zer.append(j)
                    row_zer.append(i)
        


        for i in row_zer:

            matrix[i] = [0 for i in range(len(matrix[0]))]
        


        for i in col_zer:

            for j in range(len(matrix)):
                matrix[j][i] = 0





        