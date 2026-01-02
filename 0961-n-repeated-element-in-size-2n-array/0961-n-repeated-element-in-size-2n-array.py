class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        secik = set()

        for i in nums:
            if i in secik:
                return i
            else:
                secik.add(i)
