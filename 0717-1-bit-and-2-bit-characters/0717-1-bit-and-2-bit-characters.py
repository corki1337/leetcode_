class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        dl = len(bits)
        while i < dl:
            if i == dl - 2:
                if bits[i] == 0:
                    return True
                else:
                    return False
            elif i == dl -1:
                return True
            else:
                if bits[i] == 1:
                    i += 2
                else:
                    i += 1
        return False