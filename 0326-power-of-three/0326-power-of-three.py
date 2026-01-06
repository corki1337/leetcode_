class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return True if 3**21 % n == 0 else False