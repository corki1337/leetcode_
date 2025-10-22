class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        secik = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] in {'1','2','3','4','5','6','7','8','9'}:
                    if board[i][j] not in secik:
                        secik.add(board[i][j])
                    else:
                        return False
            secik.clear()
        
        for i in range(0,9):
            for j in range(0,9):
                if board[j][i] in {'1','2','3','4','5','6','7','8','9'}:
                    if board[j][i] not in secik:
                        secik.add(board[j][i])
                    else:
                        return False
            secik.clear()
        indeks = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for _ in range(9):
                    if board[i + indeks//3][j + indeks%3] in {'1','2','3','4','5','6','7','8','9'}:
                        if board[i + indeks//3][j + indeks%3] not in secik:
                            secik.add(board[i + indeks//3][j + indeks%3])
                            
                        else:
                            return False
                    indeks +=1
                indeks = 0    
                secik.clear()
        return True

        
        