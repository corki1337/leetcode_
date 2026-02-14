class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t[0]
        
        slowniks = dict()
        
        for i in s:
            if i in slowniks:
                slowniks[i] += 1
            else:
                slowniks[i] = 1

        for i in t:
            if i in slowniks:

                if slowniks[i] == 1:
                    del slowniks[i]
                else:
                    slowniks[i] -=1
            else:
                return i