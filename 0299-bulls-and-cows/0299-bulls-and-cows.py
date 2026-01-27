class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        byczq = 0
        krowy = 0
        sekret = dict()
        strzal = dict()


        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                byczq += 1
            else:
                if secret[i] in sekret:
                    sekret[secret[i]] += 1
                else:
                    sekret[secret[i]] = 1
                if guess[i] in strzal:
                    strzal[guess[i]] += 1
                else:
                    strzal[guess[i]] = 1
        
        for i in sekret:
            if i in strzal:
                krowy += min(sekret[i], strzal[i])




        return f"{byczq}A{krowy}B"

        
