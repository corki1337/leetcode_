class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        dl = len(stones)
        while True > 0:
            maks1 = [0,0]
            maks2 = [0,0]
            for i in range(dl):
                if stones[i] > maks1[0]:
                    maks2 = maks1
                    maks1 = [stones[i], i]
                elif stones[i] >= maks2[0]:
                    maks2 = [stones[i], i]
            if min(maks1[0], maks2[0]) !=0:
                if maks1[0] == maks2[0]:
                    stones[maks1[1]] = 0
                    stones[maks2[1]] = 0
                else:
                    stones[maks2[1]] = 0
                    stones[maks1[1]] = maks1[0] - maks2[0]
            else:
                return max(stones)
        