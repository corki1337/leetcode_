class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2
            return 
        if n == 0:
            return 


        mp = m -1 
        np = n -1

        for i in range(m + n -1, -1, -1):
            
            if np >= 0 and (mp < 0 or nums2[np] > nums1[mp]):
                nums1[i] = nums2[np]
                np -= 1
            else:
                nums1[i] = nums1[mp]
                mp-=1
        
