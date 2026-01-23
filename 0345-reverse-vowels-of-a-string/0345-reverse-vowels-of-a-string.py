class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels = {'a', 'e', 'i', 'o', 'u'}

        p1 = 0
        p2 = len(s)-1

        ans = ""
        vovels2 = []
        p3 = 0
        aaaa = False
        while p2 - p1 > 0:

            if s[p1].lower() in vovels:
                if s[p2].lower() in vovels:
                    ans += s[p2]
                    vovels2.append(s[p1])
                    vovels2
                    p1 += 1
                    p2 -= 1
                else:
                    p2 -= 1
            else:
                ans += s[p1]
                p1 += 1
        if p1 == p2:
            ans += s[p1]
            aaaa = True
        if not vovels2:
            return s

        if not aaaa:
            for i in range(max(p1,p2), len(s)):
                if s[i].lower() in vovels:
                    ans += vovels2[-1-p3]
                    p3 += 1
                else:
                    ans += s[i]
        else:
            for i in range(max(p1,p2) + 1, len(s)):
                if s[i].lower() in vovels:
                    ans += vovels2[-1-p3]
                    p3 += 1
                else:
                    ans += s[i]

        return ans





        