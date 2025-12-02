class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minimum = len(strs[0])
        for i in strs:
            if not i:
                return ""
            
            if minimum > len(i):
                minimum = len(i)

        ans = ""
        act = ''
        
        for i in range(0, minimum):
            act = strs[0][i]
            for j in strs:
                if act != j[i]:
                    return ans
            ans += act
                
        return ans
