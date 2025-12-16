class Solution:
    def intToRoman(self, num: int) -> str:

        ans = ""
        slowniczek1 ={
            1 : 'I',
            2 : 'X',
            3 : 'C',
            4 : 'M'
        }
        slowniczek2 ={
            1 : 'V',
            2 : 'L',
            3 : 'D'
        }

        stringuch = str(num)
        dl = len(stringuch)
        for i in range(dl):
            cyfra = int(stringuch[i])
            wyk =  dl-1-i
            
            if cyfra >= 1 and cyfra <= 3:
                ans += cyfra*slowniczek1[wyk+1]
            elif cyfra == 4:
                ans += slowniczek1[wyk+1] + slowniczek2[wyk+1]
            elif cyfra == 5:
                ans += slowniczek2[wyk+1]
            elif cyfra > 5 and cyfra <= 8:
                ans += slowniczek2[wyk+1] + (cyfra-5) * slowniczek1[wyk+1]
            elif cyfra == 9:
                ans += slowniczek1[wyk+1] + slowniczek1[wyk+2]
        return ans

        