class Solution:
    def romanToInt(self, s: str) -> int:
        slownik = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        wynik = 0
        for i in range(len(s)-1):
            if slownik[s[i]] >= slownik[s[i+1]]:
                wynik += slownik[s[i]]
            else:
                wynik -= slownik[s[i]]
        
        return wynik + slownik[s[-1]]