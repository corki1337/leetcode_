class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                pass
            elif nums[i] % 3 == 1:
                nums[i] -= 1
                ans += 1
            elif nums[i] % 3 == 2:
                nums[i] += 1
                ans += 1
        return ans
        