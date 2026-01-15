class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(set(nums)) < 3 :
            return max(nums)
        elif len(set(nums)) == 3:
            return min(nums)


        liczby = [nums[0], nums[1], nums[2]]
        liczby.sort(reverse = True)
        for i in nums:
            if i in liczby:
                continue
            if i >= liczby[2]:
                if i < liczby[1]:
                    liczby[2] = i
                elif i < liczby[0]:
                    liczby[2] = liczby[1]
                    liczby[1] = i
                else:
                    liczby[2] = liczby[1]
                    liczby[1] = liczby[0]
                    liczby[0] = i

            else:
                continue

        return liczby[2]