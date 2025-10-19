class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        trojkat = [[1], [1, 1]]
        for i in range(2, numRows):
            trojkat.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    trojkat[i].append(1)
                else:
                    trojkat[i].append(trojkat[i-1][j-1] + trojkat[i-1][j])



        return trojkat