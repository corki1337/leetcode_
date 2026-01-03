class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        mapka = dict()

        for i in s:
            if i in mapka:
                mapka[i] += 1
            else:
                mapka[i] = 1
        
        for i in range(len(s)):
            if mapka[s[i]] ==1:
                return i
        return -1