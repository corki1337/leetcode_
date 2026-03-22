class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

        for i in range(4):
            if mat == target:
                return True
            
            def transodwr(matrix):
                dlug = len(matrix)
                for i in range(dlug):
                    for j in range(dlug-i-1):
                        matrix[i][j] ^= matrix[dlug - 1 - j][dlug -1 -i]
                        matrix[dlug - 1 - j][dlug -1 -i] ^= matrix[i][j]
                        matrix[i][j] ^= matrix[dlug - 1 - j][dlug -1 -i]
                return matrix
            def flip(matrix):
                for i in range(len(matrix)//2):
                    matrix[i], matrix[len(matrix) -1-i] = matrix[len(matrix)-1-i], matrix[i]
                return matrix
            mat = transodwr(mat)
            mat = flip(mat)
        return False