class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        slownik = {}

        for i in nums:
            if i in slownik:
                slownik[i] += 1
            else:
                slownik[i] = 1
        ans = 0
        maks = 0
        for i in slownik.values():
            if i > maks:
                maks = i

        for i in slownik.values():
            if i == maks:
                ans += i
        return ans