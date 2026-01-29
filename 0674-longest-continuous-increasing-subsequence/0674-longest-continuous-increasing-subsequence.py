class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        

        ans = 1
        akt = 1
        for i in range(len(nums)-1):

            if nums[i+1] - nums[i] > 0:
                akt += 1
            else:
                if akt > ans:
                    ans = akt
                akt = 1
        return akt if akt > ans else ans