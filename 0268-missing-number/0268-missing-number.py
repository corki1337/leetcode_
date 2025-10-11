class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        suma = 0
        maxuch = 0
        for i in nums:
            suma += i
            if i > maxuch:
                maxuch = i
        if len(nums)-1 == maxuch:
            return maxuch +1
        else:
            return int((maxuch/2) * (len(nums)+1) - suma)
