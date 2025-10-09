class Solution:
    def isPalindrome(self, s: str) -> bool:
        str =""
        for i in s:
            i = i.lower()
            if i in "qwertyuiopasdfghjklzxcvbnm0123456789":
                str += i
        if str =="" or str == str[::-1]:
            return True
        else:
            return False
            
            