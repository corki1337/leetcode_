class Solution:
    def binaryGap(self, n: int) -> int:
        binuch = str(bin(n))[2:]
        ans = 0
        akt = 0
        przerwa = False
        for i in binuch:
            if przerwa:
                if i == '0':
                    akt +=1
                else:
                    if akt > ans:
                        ans = akt
                    akt = 1
            else:
                if i == '1':
                    przerwa = True
                    akt = 1
        return ans
            