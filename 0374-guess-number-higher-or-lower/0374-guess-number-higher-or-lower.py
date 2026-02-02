# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        

        l= 0
        p = n

        while p-l >= 2:
            wynik = guess((l+p)//2)
            if wynik == 0:
                return (l+p)//2
            elif wynik == 1:
                l = (l+p)//2
            else:
                p = (l+p)//2
        
        if guess(l) == 0:
            return l
        else:
            return p
