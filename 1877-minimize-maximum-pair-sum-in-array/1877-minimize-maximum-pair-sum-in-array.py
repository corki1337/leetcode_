class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        posortowane = nums.sort()

        maksuch = 0

        for i in range(0, len(nums)//2):
            if maksuch < nums[i] + nums[-1-i]:
                maksuch = nums[i] + nums[-1-i]
        return maksuch
        