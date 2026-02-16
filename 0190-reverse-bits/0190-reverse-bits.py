class Solution:
    def reverseBits(self, n: int) -> int:
        binarnie = str(bin(n))[2:]
        dlugosc = len(binarnie)

        binarnie = ("0" * (32-dlugosc)) + binarnie

        return int((binarnie)[::-1], 2)
