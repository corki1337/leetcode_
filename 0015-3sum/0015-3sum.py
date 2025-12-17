class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        hashish = {}
        for i in range(len(nums)):

            hashish[nums[i]] = i
        
        if len(set(nums)) == 1:
            if nums[0] == 0:
                return [[0,0,0]]

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if -nums[i] - nums[j] in hashish:
                    if hashish[-nums[i] - nums[j]] > j:
                        trojka = tuple(sorted([nums[i], nums[j], -nums[i] - nums[j]]))
                        ans.add(trojka)

        return list(ans)


