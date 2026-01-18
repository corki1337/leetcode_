class Solution:

    def czymagiczny(self, grid : List[List[int]]):

        ilrow = len(grid)
        ilcol = ilrow


        sumka = sum(grid[0])

        for r in range(ilrow):
            aktsum = 0

            for c in range(ilcol):
                
                aktsum += grid[r][c]

            if aktsum != sumka:
                return False
        

        for r in range(ilrow):
            aktsum = 0

            for c in range(ilcol):
                
                aktsum += grid[c][r]

            if aktsum != sumka:
                return False
        aktsum1 = 0
        aktsum2 = 0
        for i in range(ilrow):

            aktsum1 += grid[i][i]
            aktsum2 += grid[i][-i-1]


        if aktsum1 != sumka or aktsum2 != sumka:
            return False
        
        return True










    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        najw = 1
        ilrow = len(grid)
        ilcol = len(grid[0])

        najwk = min(ilrow, ilcol)

        for k in range(najwk , 1, -1):


            for row in range(0, ilrow - k+1):
                for col in range(0, ilcol - k+1):

                    if self.czymagiczny([wiersz[col:col+k] for wiersz in grid[row:row+k]]):
                        return k
        return 1
