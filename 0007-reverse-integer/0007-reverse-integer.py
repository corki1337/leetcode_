class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(x)[::-1]) if str(x)[0] != '-' else int('-' + str(x)[:0:-1])
        return ans if ans <= 2**31 -1 and ans >= -1 * 2**31 else 0