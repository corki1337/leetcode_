class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        najm = nums[0]
        for i in nums:
            if abs(i) < abs(najm):
                najm = i
            elif najm < 0 and najm * (-1) == i:
                najm = i
        return najm