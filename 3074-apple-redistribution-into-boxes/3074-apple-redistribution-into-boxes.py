class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        jablka = sum(apple)

        capacity.sort(reverse=True)
        
        cap =0
        icznik = 0
        for i in capacity:
            icznik += 1
            cap += i
            if cap >= jablka:
                return icznik
                

        