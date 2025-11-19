class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in nums:
            if i == original:
                original *= 2
            elif i > original:
                return original
        return original