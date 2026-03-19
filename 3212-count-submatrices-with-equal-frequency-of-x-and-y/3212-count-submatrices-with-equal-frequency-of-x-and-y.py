class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:



        czybylo = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        ans = 0
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    if grid[row][col] == 'X':
                        grid[row][col] = 1
                        czybylo[row][col] = 1
                    elif grid[row][col] == 'Y':
                        grid[row][col] = -1
                        czybylo[row][col] = 1
                    else:
                        grid[row][col] = 0
                elif row == 0:
                    if grid[row][col] == 'X':
                        czybylo[row][col] = czybylo[row][col-1] | 1
                        grid[row][col] = grid[row][col-1] + 1
                        
                    elif grid[row][col] == 'Y':
                        czybylo[row][col] = czybylo[row][col-1] | 1
                        grid[row][col] = grid[row][col-1] -1
                        
                    else:
                        czybylo[row][col] = czybylo[row][col-1] | 0
                        grid[row][col] = grid[row][col-1] 
                elif col == 0:
                    if grid[row][col] == 'X':
                        czybylo[row][col] = czybylo[row-1][col] | 1
                        grid[row][col] = grid[row-1][col] + 1
                        
                    elif grid[row][col] == 'Y':
                        czybylo[row][col] = czybylo[row-1][col] | 1
                        grid[row][col] = grid[row-1][col] -1
                        
                    else:
                        czybylo[row][col] = czybylo[row-1][col] | 0
                        grid[row][col] = grid[row-1][col]
                else:
                    if grid[row][col] == 'X':
                        czybylo[row][col] = czybylo[row-1][col] | 1 | czybylo[row][col-1]
                        grid[row][col] = grid[row-1][col] + 1 - grid[row-1][col-1] + grid[row][col-1]
                        
                    elif grid[row][col] == 'Y':
                        czybylo[row][col] = czybylo[row-1][col] | 1 | czybylo[row][col-1]
                        grid[row][col] = grid[row-1][col] - 1 - grid[row-1][col-1] + grid[row][col-1]
                        
                    else:
                        czybylo[row][col] = czybylo[row-1][col] | 0 | czybylo[row][col-1]
                        grid[row][col] = grid[row-1][col]- grid[row-1][col-1] + grid[row][col-1]               
                if czybylo[row][col] and not grid[row][col]:
                    ans +=1
        return ans 