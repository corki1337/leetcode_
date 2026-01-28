class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        dl = len(nums)
        if dl < 3:
            return 0

        p1 = 0
        p2 = 2
        ans = 0
        popr = nums[1] - nums[0]

        while p2 < dl:
            

            aktr = nums[p2] - nums[p2-1]

            if aktr == popr:
                p2 += 1
                continue

            else:
                if p2-p1 >= 3:

                    ans += int((p2-p1-2)*((p2-p1-1)/2))
                
                p1 = p2-1
                popr = aktr
                
                

        if p2-p1 >=3:
            ans += int((p2-p1-2)*((p2-p1-1)/2))
            
        return ans