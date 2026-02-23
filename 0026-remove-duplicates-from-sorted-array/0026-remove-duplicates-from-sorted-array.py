class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        pop = nums[0]
        l = 1
        p = 1
        dlug = len(nums)

        while p < dlug:

            if pop != nums[p]:

                nums[l] = nums[p]
                pop = nums[p]
                l += 1
            p += 1
        
        return l