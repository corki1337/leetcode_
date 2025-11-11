class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        nowy = s + s
        for i in range(len(s)):
            if nowy[i] == goal[0]:
                for j in range(len(goal)):
                    if nowy[i+j] == goal[j]:
                        if j == len(goal)-1:
                            return True
                    else:
                        break
        return False
                    