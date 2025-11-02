class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        licznik = 1
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                licznik +=1
            else:
                licznik = 1
            if licznik >= 3:
                pass
            else:
                ans += s[i]
        return ans
