class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        granicarow = len(matrix)-1
        granicacol = len(matrix[0])-1
        ilosc = 1
        zostalo = 4
        r = 0
        c = 1
        
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [x[0] for x in matrix]
        ans = [matrix[0][0]]
        for _ in range(2, len(matrix) * len(matrix[0])+1):


            ans.append(matrix[r][c])

            if zostalo == 4:
                if ilosc == granicacol:
                    ilosc = 1
                    r +=1
                    zostalo -=1
                else:
                    c +=1
                    ilosc +=1

            

            elif zostalo ==3:
                if ilosc ==granicarow:
                    ilosc = 1
                    c -=1
                    zostalo -=1
                else:
                    r +=1
                    ilosc +=1


            elif zostalo ==2:
                if ilosc ==granicacol:
                    ilosc = 1
                    r -=1
                    zostalo -=1
                else:
                    c -= 1
                    ilosc +=1

                
            elif zostalo ==1:
                if ilosc ==granicarow-1:
                    ilosc = 0
                    c +=1
                    zostalo = 4
                    granicarow -= 2
                    granicacol -= 2

                else:
                    r -= 1
                    ilosc +=1
        


        return ans

