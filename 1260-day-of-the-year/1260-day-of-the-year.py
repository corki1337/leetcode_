class Solution:
    def dayOfYear(self, date: str) -> int:
        miesiac = int(date[5:7])
        dzien = int(date[8:10])
        rok = int(date[0:4])
        dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if miesiac <= 2:
            if miesiac == 1:
                return dzien
            else:
                return dzien + 31
        else:
            if rok % 4 ==0 and (not rok % 100 == 0 or rok % 400 == 0):
                dni[1] = 29
            for i in range(miesiac-1):
                dzien += dni[i]
        return dzien


        