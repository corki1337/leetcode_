class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <1:
            return False
        for i in str(bin(n-1))[2:]:
            if i == '0':
                return False
        return True