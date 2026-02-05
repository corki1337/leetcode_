class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        dlug = len(nums)
        for i in range(dlug):
            przes = nums[i]
            if przes > 0:
                przes = (i + przes) % dlug
            elif przes < 0:
                przes = abs(przes) % dlug
                przes =  (i - przes) % dlug
            else:
                przes = i 
            ans.append(nums[przes])
        return ans


