class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = 0
        p = len(nums)-1
        if p == 0:
            return 0

        

        while p-l >= 2:
            
            if nums[(p+l)//2] > nums[(p+l)//2 - 1]:
                l = (p+l)//2
            else:
                p = (p+l)//2
        
        if l == 0:
            return 0 if nums[0] > nums[1] else p
        elif p == len(nums) -1:
            return p if nums[p] > nums[p-1] else l
        else:
            return p -1
        