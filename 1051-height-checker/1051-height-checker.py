class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        posortowana = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != posortowana[i]:
                ans += 1
        return ans