class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        secik = set()
        ans = []
        for i in nums:
            if i in secik:
                ans.append(i)
            else:
                secik.add(i)
        return ans