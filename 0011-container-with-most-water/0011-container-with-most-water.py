class Solution:
    def maxArea(self, height: List[int]) -> int:
        maks = 0 
        poczatek = 0
        koniec = len(height) - 1
        while poczatek != koniec:
            if height[poczatek] <= height[koniec]:
                if maks < (koniec - poczatek) * height[poczatek]:
                    maks = (koniec - poczatek) * height[poczatek]
                poczatek += 1
            else:
                if maks < (koniec - poczatek) * height[koniec]:
                    maks = (koniec - poczatek) * height[koniec]
                
                koniec -= 1
        return maks

                