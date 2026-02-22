class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        zero = s[0]

        l = 0
        p = 1
        
        pop = s[0]
        
        for i in range(1, len(s)):
            if s[i] != pop:
                p = i
                break
        else:
            return 0
        ans = 0
        popdlug = p
        aktdlug = 0
        pop = str((int(pop) * (-1)) + 1)

        while p < len(s):
            if s[p] != pop:

                akt = min(popdlug, aktdlug)
                ans += akt
                l += akt
                pop = s[p]
                popdlug = aktdlug
                aktdlug = 0

            p += 1
            aktdlug += 1
        

        return ans + min(popdlug, aktdlug)

