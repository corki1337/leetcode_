class Solution:
    def findLucky(self, arr: List[int]) -> int:
        slownik = dict()
        ans = -1
        for i in arr:
            if i not in slownik:
                slownik[i] = 1
            else:
                slownik[i] += 1
        for i in slownik.keys():
            if i == slownik[i]:
                if ans < i:
                    ans = i

        return ans