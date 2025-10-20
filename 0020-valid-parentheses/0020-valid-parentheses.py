class Solution:
    def isValid(self, s: str) -> bool:
        nawias = []
        if s == "":
            return True
        for i in s:
            if i in ('(', '{', '['):
                nawias.append(i)
            elif nawias != []:
                if (i == ')' and nawias[-1] == '(') or (i == '}' and nawias[-1] == '{') or (i == ']' and nawias[-1] == '['):
                    nawias.pop()
                else:
                    return False
            else:
                return False
        if nawias != []:
            return False
        return True