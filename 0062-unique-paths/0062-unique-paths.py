class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def silnia(n):
            return 1 if n <= 1 else silnia(n-1) * n

        #return dwumiannewtona (m+n-2) po m-1

        return silnia(m+n-2)//(silnia(m-1) * silnia(m+n-2-m+1))