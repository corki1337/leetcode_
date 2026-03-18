class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        row = 0
        if grid[0][0] > k:
            return 0
        while row < len(grid):
            sumka = 0
            col = 0
            while col < len(grid[0]):
                if col ==0 and row ==0:
                    pass
                elif col == 0 and row!= 0:
                    grid[row][col] += grid[row-1][col]
                elif row == 0:
                    grid[row][col] += grid[row][col-1]
                else:
                    grid[row][col] += grid[row][col-1] + grid[row-1][col] - grid[row-1][col-1]
                if grid[row][col] <= k:
                    ans +=1
                else:
                    break



                col += 1
            row += 1
        return ans