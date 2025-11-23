class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altka = [0]
        for i in range(len(gain)):
            altka.append(gain[i]+altka[i])
        return max(altka)