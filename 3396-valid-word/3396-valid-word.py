class Solution:
    def isValid(self, word: str) -> bool:
        vow = False
        cons = False
        if len(word) < 3:
            return False
        else:
            for i in word:
                if i in {'1','2','3','4','5','6','7','8','9','0'}:
                    pass
                elif i.lower() in {'a', 'e', 'i', 'o', 'u'}:
                    vow = True
                elif i.upper() in {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}:
                    cons = True
                else:
                    return False
        return vow and cons
