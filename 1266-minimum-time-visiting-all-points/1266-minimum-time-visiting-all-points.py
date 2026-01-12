class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:


        ans = 0
        popo = points[0]
        for i in points:
            

            ans += max(abs(popo[0] - i[0]), abs(i[1] - popo[1]))
            popo = i


        return ans
        