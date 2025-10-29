class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = ""
        for _ in range(len(bin(n))-2):
            ans +="1"
        return int(ans, 2)