class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        ans = 0
        for i in nums:
            dzielnik = 2
            dzielnik1 = 1
            dzielnik2 = 1
            znal = False
            
            if int(sqrt(i)) == sqrt(i):
                continue

            while dzielnik ** 2 <= i:
                
                if i % dzielnik == 0:

                    if not znal:
                        dzielnik1 = dzielnik
                        dzielnik2 = i//dzielnik
                        znal = True
                        ans += 1 + i + dzielnik1 + dzielnik2
                    else:
                        ans -= 1 + i + dzielnik1 + dzielnik2
                        break
                dzielnik += 1



        return ans
        
                    