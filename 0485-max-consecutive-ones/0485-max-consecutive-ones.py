class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0 
        akt = 0

        for i in nums:
            
            if i == 1:
                akt += 1
            else:
                if ans < akt:
                    ans = akt
                
                akt = 0
            
        return akt if akt > ans else ans