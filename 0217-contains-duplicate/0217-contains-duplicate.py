class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        zbior = set()
        for i in nums:
            if i in zbior:
                return True
            else:
                zbior.add(i)
        return False