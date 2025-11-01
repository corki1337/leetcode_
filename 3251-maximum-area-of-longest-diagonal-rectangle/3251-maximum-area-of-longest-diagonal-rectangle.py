class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        najd = 0
        pole = 0
        for i in dimensions:
            if sqrt(i[0] ** 2 + i[1] ** 2) < najd:
                pass
            elif sqrt(i[0] ** 2 + i[1] ** 2) == najd:
                if  pole < i[0] * i[1]:

                    pole = i[0] * i[1]
                    najd = sqrt(i[0] ** 2 + i[1] ** 2)
            else:
                pole = i[0] * i[1]
                najd = sqrt(i[0] ** 2 + i[1] ** 2)
        return pole


