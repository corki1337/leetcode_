class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        if len(s) <= 2:
            return True

        czyzero = False

        for i in s[1:]:
            if czyzero and i == '1':
                return False
            elif not czyzero and i =='0':
                czyzero = True
        return True
