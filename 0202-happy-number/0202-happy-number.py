class Solution:
    def isHappy(self, n: int) -> bool:
        zbior = {1}
        while True:
            liczba = 0
            for i in str(n):
                liczba += (int(i))**2
            n = liczba
            if n == 1:
                return True
            elif n in zbior:
                return False
            else:
                zbior.add(n)
        