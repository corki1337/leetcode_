class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        liczba = 0
        for i in operations:
            if i[1] == '+':
                liczba += 1
            else:
                liczba -= 1
        return liczba