class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            return 0
        

        nums.sort()


        minimum = 10**5
        for i in range(0, len(nums)-k+1):
            if nums[i+k-1] - nums[i] < minimum:
                minimum = nums[i+k-1] - nums[i] 
        return minimum

        