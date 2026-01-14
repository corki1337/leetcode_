class Solution:
    def findComplement(self, num: int) -> int:
        

        dlug = len(bin(num)[2:])
        numa = 2**dlug - 1
        return numa ^ num