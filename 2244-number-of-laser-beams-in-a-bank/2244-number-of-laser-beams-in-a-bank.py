class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        swiecie = False
        ans = 0
        poprz = 0
        
        for i in bank:
            currsum = 0 
            for j in i:
                if j == '1':
                    currsum += 1
            if swiecie == False:
                poprz = currsum
                swiecie = True
            elif currsum != 0:
                ans += currsum * poprz
                swiecie = True
                poprz = currsum

        return ans