class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]


        def silnia(n):
            if n == 0:
                return 1
            elif n == 1:
                return 1
            else:
                return n * silnia(n-1)

        icznik = silnia(rowIndex)
        if rowIndex % 2 == 1:
            
            tablica = [icznik//(silnia(i) * silnia(rowIndex-i)) for i in range(0, rowIndex//2 + 1)]
            return tablica + tablica[::-1]
        else:
            tablica = [icznik//(silnia(i) * silnia(rowIndex -i)) for i in range(0, rowIndex//2 + 1)]
            return tablica[:-1:] + tablica[::-1]