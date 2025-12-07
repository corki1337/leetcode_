class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        return (high - low)//2  + high%2 if low % 2 == 0 else (high - low)//2 + 1
