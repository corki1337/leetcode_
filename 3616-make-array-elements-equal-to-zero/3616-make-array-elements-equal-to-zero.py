class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ilosc = 0
        znak = 1

        
        for i in range(len(nums)):
            if nums[i] == 0:
                kopia = nums[:]
                curr = i
                znak = 1
                while curr < len(kopia) and curr >= 0:

                    if kopia[curr] != 0:  
                        kopia[curr] -= 1
                        znak *= -1
                    if znak > 0:
                        curr += 1
                    else:
                        curr -= 1

                if set(kopia) == {0}:
                    ilosc += 1

                kopia = nums[:]
                curr = i
                znak = -1
                while curr < len(kopia) and curr >= 0:

                    if kopia[curr] != 0:  
                        kopia[curr] -= 1
                        znak *= -1                
                    if znak > 0:
                        curr += 1
                    else:
                        curr -= 1
                if set(kopia) == {0}:
                    ilosc += 1

            else:
                pass




        return ilosc
