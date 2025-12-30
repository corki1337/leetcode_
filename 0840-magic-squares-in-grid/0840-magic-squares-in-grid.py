class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        rowki = len(grid)
        kolki = len(grid[0])
        ans = 0
        if rowki < 3 or kolki < 3:
            return ans
        

        for row in range(0, rowki -2):
            for col in range(0, kolki -2):
                zbior = set()
                if grid[row][col] in zbior:
                    continue
                zbior.add(grid[row][col])
                if grid[row][col+1]in zbior:
                    continue
                zbior.add(grid[row][col+1])
                if grid[row][col+2] in zbior:
                    continue
                zbior.add(grid[row][col+2])
                if grid[row+1][col] in zbior:
                    continue
                zbior.add(grid[row+1][col])
                if grid[row+1][col+1] in zbior:
                    continue
                zbior.add(grid[row+1][col+1])
                if grid[row+1][col+2] in zbior:
                    continue
                zbior.add(grid[row+1][col+2])
                if grid[row+2][col] in zbior:
                    continue
                zbior.add(grid[row+2][col])
                if grid[row+2][col+1] in zbior:
                    continue
                zbior.add(grid[row+2][col+1])
                if grid[row+2][col+2] in zbior:
                    continue
                zbior.add(grid[row+2][col+2])
                if zbior != {1,2,3,4,5,6,7,8,9}:
                    continue

                sumka = grid[row][col] + grid[row][col+1] + grid[row][col+2]
                if sumka != grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2]:
                    continue
                if sumka != grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]:
                    continue
                if sumka != grid[row][col] + grid[row+1][col] + grid[row+2][col]:
                    continue
                if sumka != grid[row][col+1] + grid[row+1][col+1] + grid[row+2][col+1]:
                    continue
                if sumka != grid[row][col+2] + grid[row+1][col+2] + grid[row+2][col+2]:
                    continue
                if sumka != grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]:
                    continue
                if sumka != grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]:
                    continue
                ans +=1

        return ans