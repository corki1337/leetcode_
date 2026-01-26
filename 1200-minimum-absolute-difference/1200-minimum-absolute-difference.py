class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        minimuch = arr[1] - arr[0]
        for i in range(0, len(arr) - 1):
            if minimuch > -arr[i] + arr[i+1]:
                minimuch = -arr[i] + arr[i+1]
        
        ans = []

        for i in range(0, len(arr) - 1):

            if -arr[i] + arr[i+1] == minimuch:
                ans.append([arr[i], arr[i+1]])
        return ans
        