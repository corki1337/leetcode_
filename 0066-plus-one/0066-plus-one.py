class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        liczba = 0
        for i in range(len(digits)):
            liczba += 10**i *digits[-i-1]
        liczba += 1
        return [int(i) for i in str(liczba)]
