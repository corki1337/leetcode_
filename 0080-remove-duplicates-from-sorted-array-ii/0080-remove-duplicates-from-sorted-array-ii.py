class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        zapis = 0
        odczyt = 0
        pop = ''
        ilosc = 0
        dlugosc = len(nums)

        while odczyt < dlugosc:

            if nums[odczyt] == pop:
                ilosc += 1
                if ilosc > 2:
                    pass
                else:
                    nums[zapis] = nums[odczyt]
                    pop = nums[odczyt]
                    zapis +=1
            else:
                nums[zapis] = nums[odczyt]
                pop = nums[odczyt]
                ilosc = 1
                zapis += 1

            odczyt += 1

        return zapis
            