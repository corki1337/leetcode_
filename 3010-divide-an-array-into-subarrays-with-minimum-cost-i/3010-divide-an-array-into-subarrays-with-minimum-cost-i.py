class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        dl = len(nums)

        if dl == 3:
            return sum(nums)

        najm = [nums[1], nums[2]] if nums[1] < nums[2] else [nums[2], nums[1]]


        for i in nums[3:]:
            if i < najm[1]:
                if i < najm[0]:
                    najm[1] = najm[0]
                    najm[0] = i
                else:
                    najm[1] = i
        return nums[0] + sum(najm)



