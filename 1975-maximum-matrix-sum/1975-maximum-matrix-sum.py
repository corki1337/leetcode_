class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        najm = matrix[0][0]
        mn = 0
        suma = 0

        for i in matrix:
            for j in i:
                
                if j < 0:
                    l = -1*j
                    mn += 1
                    if -1 * j < abs(najm):
                        najm = -1 * j
                else:
                    l = j
                    if j < abs(najm):
                        najm = j
                suma += l
        if mn%2 == 0:
            return suma
        else:
            return suma - 2 * abs(najm)