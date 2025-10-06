class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        dl = 0
        ost = False
        for i in range(len(s)):
            if s[-i-1] ==' ' and not ost:
                pass
            elif s[-i-1] ==' ' and ost:
                return dl
            else:
                dl +=1
                ost = True
        return dl


