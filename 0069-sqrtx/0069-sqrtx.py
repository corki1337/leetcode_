class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        p = 0
        k = 2**31 -1
        while p != k:
            lic = int((p+k)/2)
            pot = lic**2
            if pot == x:
                return lic
            elif (lic-1)**2 < x and pot > x:
                return lic-1
            elif pot < x:
                p = lic
            else:
                k = lic