class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        lancuch = ""
        ans= []
        for i in nums:
            lancuch += str(i)
            if int(lancuch, 2) % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)

        return ans