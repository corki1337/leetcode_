class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = 10**9
        wynik = -1
        for i in nums:

            
            if abs(i - mini) > wynik and i > mini:
                wynik = abs(i - mini)

            if mini > i:
                mini = i

        return wynik
