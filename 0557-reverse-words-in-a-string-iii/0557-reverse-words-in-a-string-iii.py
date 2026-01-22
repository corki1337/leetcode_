class Solution:
    def reverseWords(self, s: str) -> str:

        p1 = 0
        p2 = 0
        dlug = len(s)
        s = list(s)
        while p2 < dlug:
            if s[p2] == ' ':
                for i in range(p1, p1 + (p2-p1)//2):
                    s[i] = ord(s[i])
                    s[p2-1-i+p1] = ord(s[p2-1-i+p1])
                    s[i] = s[i]^s[p2-1-i+p1]
                    s[p2-1-i+p1] = s[i]^s[p2-1-i+p1]
                    s[i] = s[i]^s[p2-1-i+p1]
                    s[i] = chr(s[i])
                    s[p2-1-i+p1] = chr(s[p2-1-i+p1])
                p1 = p2 + 1
            p2 += 1
        for i in range(p1, p1 + (p2-p1)//2):
            s[i] = ord(s[i])
            s[p2-1-i+p1] = ord(s[p2-1-i+p1])
            s[i] = s[i]^s[p2-1-i+p1]
            s[p2-1-i+p1] = s[i]^s[p2-1-i+p1]
            s[i] = s[i]^s[p2-1-i+p1]
            s[i] = chr(s[i])
            s[p2-1-i+p1] = chr(s[p2-1-i+p1])
        return ''.join(s)


        