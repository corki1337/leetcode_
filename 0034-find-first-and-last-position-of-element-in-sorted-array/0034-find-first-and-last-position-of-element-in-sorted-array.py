class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        git = False
        l = 0
        p = len(nums) - 1
        if p ==0:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        while p - l >= 2:

            s = (p+l)//2

            if nums[s] < target:
                l = s
            else:
                p = s
        if nums[l] == target:

            ans = [l]
        else:
            ans = [p]

        l = 0
        p = len(nums) - 1
        while p - l >= 2:

            s = (p+l)//2

            if nums[s] > target:
                p = s
            else:
                l = s
        if nums[p]== target:

            ans.append(p)
        else:
            ans.append(l)

        if nums[ans[0]] == target:

            return ans
        else:
            return [-1,-1]