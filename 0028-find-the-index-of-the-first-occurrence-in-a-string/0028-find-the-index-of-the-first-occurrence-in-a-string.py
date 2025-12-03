class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        stos = len(haystack)
        wyk = len(needle)
        
        if stos == wyk:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(wyk, stos+1):
            cznik = wyk-1
            for j in range(i,i-wyk,-1):
                if needle[cznik] == haystack[j-1]:
                    cznik -=1
                else:
                    break
            
            if cznik == -1:
                return i-wyk
        return -1