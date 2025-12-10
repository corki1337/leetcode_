class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapka = dict()

        for i in magazine:
            if i in mapka:
                mapka[i] +=1
            else:
                mapka[i] = 1
        
        for i in ransomNote:
            if i in mapka:
                if mapka[i] > 0:
                    mapka[i] -= 1
                else:
                    return False
            else:
                return False
    
        return True