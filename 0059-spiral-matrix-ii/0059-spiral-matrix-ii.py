import numpy as np
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
            
        maciora = np.ones((n,n), dtype = 'uint16')
        granica = n-1
        ilosc = 1
        zostalo = 4
        r = 0
        c = 1
        pierwsze = True
        for i in range(2, n**2 + 1):

            maciora[r][c] = i

            if zostalo == 4:
                if ilosc ==granica:
                    ilosc = 1
                    r +=1
                    zostalo -=1
                else:
                    c +=1
                    ilosc +=1

            

            elif zostalo ==3:
                if ilosc ==granica:
                    ilosc = 1
                    c -=1
                    zostalo -=1
                else:
                    r +=1
                    ilosc +=1


            elif zostalo ==2:
                if ilosc ==granica:
                    ilosc = 1
                    r -=1
                    zostalo -=1
                else:
                    c -= 1
                    ilosc +=1

                
            elif zostalo ==1:
                if ilosc ==granica-1:
                    ilosc = 0
                    c +=1
                    zostalo = 4
                    granica -= 2

                else:
                    r -= 1
                    ilosc +=1
        


        return maciora.tolist()

