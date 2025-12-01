class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        secik = set()
        for i in arr:
            if i in secik:
                return True
            else:
                secik.add(2*i)
                if i%2==0:
                    secik.add(i//2)
        return False