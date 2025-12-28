class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        dlrow = len(grid[0])
        dlcol = len(grid)

        col = dlcol -1
        row = 0
        ans = 0
        while row < dlrow and col >= 0:
            if grid[col][row] >=0:
                row += 1
            else:
                ans += dlrow - row
                col -= 1
        return ans

