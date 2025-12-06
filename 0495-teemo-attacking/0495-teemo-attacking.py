class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        dl = 0
        kon = 0
        for i in timeSeries:
            if kon > i:
                dl += duration -kon + i
                kon = i + duration
            else:
                dl += duration
                kon = i + duration
        return dl

            
        
        