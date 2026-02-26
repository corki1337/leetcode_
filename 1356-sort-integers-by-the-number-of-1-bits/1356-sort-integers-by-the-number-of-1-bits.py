class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        if arr:
            lewo = []
            prawo = []
            srodek = []
            mid = arr[(0 + len(arr))//2].bit_count()
            for i in arr:
                il = i.bit_count()
                if il < mid:
                    lewo.append(i)
                elif il > mid:
                    prawo.append(i)
                else:
                    srodek.append(i)
            if srodek:
                srodek.sort()
            return self.sortByBits(lewo) + srodek + self.sortByBits(prawo)
        else:
            return []