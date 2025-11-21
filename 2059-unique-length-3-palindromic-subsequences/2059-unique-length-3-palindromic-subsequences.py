class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        alfabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        bylo = {
            s[0] : [0],
        }
        nowyslownik = {}
        suby = set()
        ilosc = 0
        for i in range(len(s)):
            if s[i] in bylo.keys():
                nowyslownik[s[i]] = [bylo[s[i]][0], i]

            else:
                bylo[s[i]] =  [i]
            

        for i in nowyslownik.values():
            for j in alfabet:
                if j in s[i[0] + 1 : i[1]]:
                    if s[i[0]] + j + s[i[0]] not in suby:
                        suby.add(s[i[0]] + j + s[i[0]])
                        ilosc += 1


        return ilosc
