class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:


        slownik1 = dict()

        for n in nums1:
            slownik1[n] = 1

        
        tablica = []
        slownik2 = dict()
        for i in nums2:
            slownik2[i] = 1

        for g in slownik1:
             if g in slownik2:
                tablica.append(g)



        return tablica