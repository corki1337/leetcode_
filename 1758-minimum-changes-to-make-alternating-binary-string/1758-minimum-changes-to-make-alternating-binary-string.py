class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        

        for i in range(len(s)):
            
            ans += i%2 != int(s[i])
        return min(ans, len(s) - ans)