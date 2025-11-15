class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            git = True
            for j in str(i):
                if j =='0':
                    git = False
                    break
                else:
                    if int(i) % int(j) == 0:
                        pass
                    else:
                        git = False
                        break
            if git:

                ans.append(int(i))
        return ans