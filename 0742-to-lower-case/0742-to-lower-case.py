class Solution:
    def toLowerCase(self, s: str) -> str:
        n = ""
        for i in s:
            n += i.lower()

        return n
