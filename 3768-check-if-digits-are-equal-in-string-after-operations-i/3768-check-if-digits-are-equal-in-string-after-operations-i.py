class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) != 2:
            string = ""
            for i in range(len(s) - 1):
                string += str((int(s[i]) + int(s[i+1])) % 10)
            s = string
        


        return True if (s[-2] == s[-1]) else False
        
