class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        mapka = dict()
        ans = 0
        for i in nums:
            if i in mapka:
                mapka[i] += 1
            else:
                mapka[i] = 1
        
        for i in mapka:
            if mapka[i] > 1:
                ans += mapka[i] * (mapka[i] -1)//2
        return ans