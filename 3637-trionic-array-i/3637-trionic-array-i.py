class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        if len(nums)<=3:
            return False

        if nums[1] <= nums[0]:
            return False
        pop = nums[0]

        przedp = True
        przedq = True

        for i in nums[1:-1]:

            if pop == i:
                return False

            if przedp:
                if i > pop:
                    pass
                else:
                    przedp = False
            elif przedq:
                if i < pop:
                    pass
                else:
                    przedq = False
            else:
                if i > pop:
                    pass
                else:
                    return False
            pop = i
        
        if przedp:
            return False
        if nums[-1] > nums[-2]:
            return True
        else:
            return False

        