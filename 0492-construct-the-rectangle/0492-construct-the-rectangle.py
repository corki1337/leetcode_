class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        for i in range(int(sqrt(area)), 1, -1):
            
            if area//i == area/i:
                return [max(i, area//i), min(i, area//i)]
        return [area, 1]