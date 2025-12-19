class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        p1 = 0
        p2 = 0
        icznik = 0
        while p2 < len(nums):

            if nums[p2] == val:
                nums[p2] = '_'
                icznik += 1



            else:
                nums[p1] = nums[p2]

                p1 += 1

            

            p2 += 1

        for i in range(p1, p2):
            nums[i] = '_'
        return len(nums) - icznik
        