class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        dl = len(nums)
        summod = True
        for i in nums:
            if i % 2 ==0:
                pass
            else:
                if not summod:
                    summod = True
                else:
                    summod = False
        
        return dl - 1 if summod else 0
