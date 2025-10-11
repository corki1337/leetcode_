# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        p = 0
        k = n
        while k-p>=2:
            sr = (p+k)//2
            if isBadVersion(sr):
                k = sr
            else:
                p = sr
        if isBadVersion(p):
            return p
        else:
            return k