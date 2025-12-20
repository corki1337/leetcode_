class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans =0
        
        for i in range(len(strs[0])):
            poprzedni = 'a'
            for j in range(len(strs)):
                if poprzedni > strs[j][i]:
                    ans +=1
                    break
                poprzedni = strs[j][i]

        return ans