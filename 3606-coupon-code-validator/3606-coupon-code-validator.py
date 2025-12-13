class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        
        
        kodzik = set(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','_'])
        linia = set(["electronics", "grocery", "pharmacy", "restaurant"])
        
        kodyslownik = {
            "electronics" : [],
            "grocery" : [],
            "pharmacy" : [],
            "restaurant" : []

        }

        for i in range(len(code)):
            j = 0
            for j in range(len(code[i])):
                if code[i][j] not in kodzik:
                    break
            if j +1 != len(code[i]):
                continue

            if businessLine[i] not in linia:
                continue
            
            if not isActive[i]:
                continue
            
            kodyslownik[businessLine[i]].append(code[i])
        
        ans1 = kodyslownik["electronics"]
        ans2 = kodyslownik["grocery"]
        ans3 = kodyslownik["pharmacy"]
        ans4 = kodyslownik["restaurant"]

        ans = []
        if ans1 != []:
            ans1.sort()
            ans += ans1
        if ans2 != []:
            ans2.sort()
            ans += ans2
        if ans3 != []:
            ans3.sort()
            ans += ans3
        if ans4 != []:
            ans4.sort()
            ans += ans4


        return ans

        
            
            