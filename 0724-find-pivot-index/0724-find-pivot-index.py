class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumka = sum(nums)
        if sumka - nums[0] == 0:
            return 0
        aktsum = nums[0]
        for i in range(1, len(nums)):
            if 2 * aktsum == sumka - nums[i]:
                return i
            aktsum += nums[i]
        return -1