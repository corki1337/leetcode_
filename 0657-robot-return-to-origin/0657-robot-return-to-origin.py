class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = 0
        v = 0
        for i in moves:
            if i == 'U':
                h += 1
            elif i == 'D':
                h -= 1
            elif i == "R":
                v += 1
            else:
                v -= 1
        return h == 0 and v == 0