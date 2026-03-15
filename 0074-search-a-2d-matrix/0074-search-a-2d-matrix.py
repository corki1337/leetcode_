class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        p = len(matrix)-1

        while p - l >= 2:
            
            srodek = (p+l)//2
            
            if matrix[srodek][0] < target:
                l = srodek
            else:
                p = srodek
        wiersz = p
        if matrix[p][0] > target:
            if matrix[l][-1] < target:
                return False
            else:
                wiersz = l
        
        l = 0 
        p = len(matrix[0]) -1

        while p - l >= 2 :
            srodek = (p+l)//2

            if matrix[wiersz][srodek] > target:
                p = srodek
            else:
                l = srodek
        if matrix[wiersz][l] == target or matrix[wiersz][p] == target:
            return True
        else:
            return False

            