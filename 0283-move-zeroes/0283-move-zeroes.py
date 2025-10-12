class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zera = len(nums)
        indeks = 0
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[indeks] = nums[i]
                indeks += 1
            else:
                zera -= 1
        for i in range(zera, len(nums)):
            nums[i] = 0
