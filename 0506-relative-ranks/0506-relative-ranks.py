class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score) == 1:
            return ["Gold Medal"]
        elif len(score) == 2:
            return ["Gold Medal", "Silver Medal"] if score[0] > score[1] else ["Silver Medal", "Gold Medal"]
        


        posortowane = sorted(score, reverse = True)

        ABG = []

        for i in score:
            
            
            if i == posortowane[0]:
                ABG.append("Gold Medal")
            elif i == posortowane[1]:
                ABG.append("Silver Medal")
            elif i == posortowane[2]:
                ABG.append("Bronze Medal")
            else:
                ABG.append(str(posortowane.index(i)+1))
        return ABG