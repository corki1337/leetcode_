class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slownik1 = dict()
        slownik2 = dict()

        for i in s:
            if i in slownik1.keys():
                slownik1[i] += 1
            else:
                slownik1[i] = 1

        for i in t:
            if i in slownik2.keys():
                slownik2[i] += 1
            else:
                slownik2[i] = 1       
        return slownik1 == slownik2