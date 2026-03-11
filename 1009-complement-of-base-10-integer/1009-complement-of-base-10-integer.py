class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        lancuch = str(bin(n))[2:]

        ans = 0

        for i in range(len(lancuch)):
            if lancuch[-1-i] == '0':
                ans += 2**i
        return ans