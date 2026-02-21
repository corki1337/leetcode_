class Solution:

    def setbits(self, n):
        ans = 0
        stri = bin(n)[2::]
        for i in stri:
            if i =='1':
                ans += 1
        return ans
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        
        for i in range(left, right +1):
            if self.setbits(i) in {2,3,5,7,11,13,17,19}:
                ans += 1
        return ans

