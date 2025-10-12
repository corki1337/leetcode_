class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p = 0
        k = len(nums) - 1
        while k - p > 1:
            mid = (p+k)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                k = mid
            else:
                p = mid

        if nums[p]  == target:
            return p
        elif nums[k] < target:
            return k+1
        elif nums[p] > target:
            return p
        else:
            return k
