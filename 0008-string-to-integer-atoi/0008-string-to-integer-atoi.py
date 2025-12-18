class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        znak = True
        pospacji = False
        
        odczyt = False
        for i in s:
            if not odczyt:
                if i == ' ':
                    continue
                else:
                    if i =='+':
                        znak = True
                        
                    elif i =='-':
                        znak = False
                        
                    elif i in ('1','2','3','4','5','6','7','8','9'):

                        ans += i
                    elif i =='0':
                        pass
                    else:
                        return 0

                    
                    odczyt = True
            else:
                if i in ('1','2','3','4','5','6','7','8','9','0'):
                    ans += i
                else:
                    break
        if ans == '':
            return 0
        ans = int(ans) if znak else -1 * int(ans)
        if ans > 2**31 -1:
            ans = 2**31 -1
        elif ans < - 2**31:
            ans = - 2**31
        return ans
                    