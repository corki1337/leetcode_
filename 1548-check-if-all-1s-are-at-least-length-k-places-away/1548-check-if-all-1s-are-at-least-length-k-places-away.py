class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        p = False
        tetmajer = 0
        for i in nums:
            if p:
                if i == 0:
                    tetmajer += 1
                else:
                    if tetmajer < k:
                        return False
                    tetmajer = 0
            elif i == 1:
                p = True



        return True

