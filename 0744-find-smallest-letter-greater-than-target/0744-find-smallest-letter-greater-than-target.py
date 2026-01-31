class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if letters[-1] <= target:
            return letters[0]

        l = 0
        p = len(letters) - 1

        while p - l > 1:
            s = (p+l)//2

            if letters[s] > target:
                p = s
            else:
                l = s
        
        return letters[l] if letters[l] > target else letters[p]