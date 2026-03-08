class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        zbior = set()
        for i in range(len(nums)):
            zbior.add(int(nums[i], base = 2))
        
        for j in range(2**16):
            if j not in zbior:
                ans = str(bin(j)[2:])
                return ''.join(['0' for i in range(len(nums) - len(ans))]) + ans