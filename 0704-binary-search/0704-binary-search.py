class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        p = len(nums)-1

        while p-l >= 2:
            srodek = (p+l)//2

            if nums[srodek] < target:
                l = srodek
            else:
                p = srodek
        
        if nums[l] == target:
            return l
        elif nums[p] == target:
            return p
        else:
            return -1