class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()
        
        ans = 0
        dl = len(happiness)
        for i in range(0, k):
            
            akt = happiness[dl - i -1] -i if happiness[dl - i -1] - i > 0 else 0

            ans += akt
        return ans