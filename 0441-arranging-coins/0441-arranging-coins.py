class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(1,n+1):
            if i > n:
                return i-1
            n -= i