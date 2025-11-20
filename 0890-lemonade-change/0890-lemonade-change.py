class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        kaska = [0,0]
        for i in bills:
            if i == 5:
                kaska[0] += 1
            elif i == 10:
                if kaska[0] == 0 :
                    return False
                else:
                    kaska[0] -= 1
                    kaska[1] += 1
            elif i == 20:
                if kaska[0] == 0:
                    return False
                else:
                    if kaska[1] == 0:
                        if kaska[0] == 1 or kaska[0] == 2:

                            return False
                        else:
                            kaska[0] -= 3
                    else:
                        kaska[0] -= 1
                        kaska[1] -= 1

        return True

