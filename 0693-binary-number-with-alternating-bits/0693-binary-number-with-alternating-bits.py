class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        binarnie = bin(n)[2:]

        zera = {i for i in binarnie[1::2]}
        if '1' in zera:
            return False
        else:
            jedynki = {i for i in binarnie[::2]}
            if '0' in jedynki:
                return False
        return True

