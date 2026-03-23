class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat[0]) * len(mat):
            return mat
        
        
        nowar = 0
        nowac = 0
        matnowa = [[0 for i in range(c)] for j in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                matnowa[nowar][nowac] = mat[i][j]
                nowac += 1
                if nowac >= c:
                    nowac =0
                    nowar += 1
        return matnowa               