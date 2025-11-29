class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        suma = sum(nums)
        if suma % 3 ==0:
            return suma
        elif suma % 3 == 1:
            najm1 = 10**4
            najm21 = 10**4
            najm22 = 10**4
            for i in nums:
                if i%3 == 1 and i < najm1:
                    najm1 = i
                elif i % 3 ==2:
                    if i < najm21:
                        najm22 = najm21
                        najm21 = i
                        
                    elif i <= najm22:
                        najm22 = i
            if najm1 > najm21 + najm22:
                if najm21 < 10**4 and najm22 < 10**4:
                    return suma - najm22 - najm21
            else:
                if najm1 < 10**4:
                    return suma - najm1
        elif suma % 3 == 2:
            najm11 = 10**4
            najm12 = 10**4
            najm2 = 10**4
            for i in nums:
                if i % 3 == 1:
                    if i < najm11:
                        najm12 = najm11
                        najm11 = i
                    elif i <= najm12:
                        najm12 = i
                elif i % 3 ==2 and i < najm2:
                    najm2 =i
            if najm2 > najm11 + najm12:
                if najm11 < 10**4 and najm12 < 10**4:
                    return suma - najm12 - najm11
            else:
                if najm2 < 10**4:
                    return suma - najm2

        return 0


        
