class Solution:
    def countTriples(self, n: int) -> int:
        
        ans = 0

        for i in range(1, n+1):
            for j in range(1, n+1):
                cpot = sqrt(int(i**2 + j**2))
                if cpot == int(cpot):
                    if cpot <= n:
                        ans += 1
        return ans
        