class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = 0
        liczba = str(num)
        zmieniona = False
        for i in range(len(str(num))):
            if liczba[i] == "6" and not zmieniona:
                ans += 9 * 10**i
                zmieniona = True
            else:
                ans += int(liczba[i]) * 10**i
        return int(str(ans)[::-1])