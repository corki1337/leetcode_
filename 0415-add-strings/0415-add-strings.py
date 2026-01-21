class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        poz = 0

        ans = ""

        dl1 = len(num1)
        dl2 = len(num2)
        
        for i in range(min(dl1, dl2)):
            sumka = int(num1[-1-i]) + int(num2[-i-1]) + poz
            
            poz = sumka // 10
            ans += str(sumka%10)
        
        dluzsze = num1 if dl1 > dl2 else num2

        for i in range(min(dl1, dl2), max(dl1, dl2)):
            sumka = int(dluzsze[-1-i]) + poz
            poz = sumka // 10
            ans += str(sumka%10)
        
        ans = ans + str(poz) if poz != 0 else ans
        

        return ans[::-1]

