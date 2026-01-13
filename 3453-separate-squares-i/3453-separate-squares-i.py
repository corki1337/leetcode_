class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        miny = squares[0][1]
        maxy = squares[0][1] 

        calkpole = 0

        for i in squares:
            if miny > i[1]:
                miny = i[1]
            if maxy < i[1] + i[2]:
                maxy = i[1] + i[2]
            
            calkpole += i[2] ** 2
        

        akty = (miny + maxy)/2
        dolp = 0
        while maxy - miny > 10**(-5):
            dolp = 0
            akty = (miny + maxy)/2

            for i in squares:

                if i[1] + i[2] <= akty:
                    dolp += i[2] ** 2
                elif i[1] >= akty:
                    pass
                else:
                    dolp += (akty - i[1]) * i[2]
            if dolp >= calkpole/2:
                maxy = akty
            else:
                miny = akty
        return miny