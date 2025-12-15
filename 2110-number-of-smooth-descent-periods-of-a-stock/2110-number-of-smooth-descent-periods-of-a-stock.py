class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        ans = 0
        dlugosc = 1
        for i in range(len(prices) - 1):

            if prices[i]- prices[i+1] == 1:
                dlugosc += 1
            else:
                ans += (dlugosc**2 + dlugosc)/2
                dlugosc = 1
        return int((dlugosc**2 + dlugosc)/2 + ans)

        