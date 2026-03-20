class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        slownik = dict()

        for i in range(len(list1)):
            slownik[list1[i]] = i
        ans = []
        mini = 1000**2
        for i in range(len(list2)):
            if list2[i] in slownik:
                if slownik[list2[i]] + i < mini:
                    ans = [list2[i]]
                    mini = slownik[list2[i]] + i
                elif slownik[list2[i]] + i > mini:
                    pass
                else:
                    ans.append(list2[i])
        return ans