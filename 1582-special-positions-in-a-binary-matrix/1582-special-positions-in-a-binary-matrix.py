class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        sumrow = [sum(i) for i in mat]
        ans = 0
        for i in range(len(sumrow)):
            
            if sumrow[i] == 1:

                for k in range(len(mat[0])):
                    if mat[i][k] == 1:

                        aktsum = sum([j[k] for j in mat])
                        if aktsum == 1:
                            ans += 1
        return ans
        