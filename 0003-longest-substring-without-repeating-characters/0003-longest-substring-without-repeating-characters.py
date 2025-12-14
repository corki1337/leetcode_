class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dlugosc = len(s)
        akt = 0
        maks = 0
        mapka = dict()
        icznik = 0
        while icznik < dlugosc:
            znak = s[icznik]
            if znak in mapka:

                if akt > maks:
                    maks = akt

                akt = icznik - mapka[znak]
                klucze = list(mapka.keys())
                for j in klucze:
                    if mapka[j] < mapka[znak]:
                        mapka.pop(j)


                mapka[znak] = icznik



            else:
                akt += 1
                mapka[znak] = icznik

            icznik += 1
        if akt > maks:
            maks = akt
        
        return maks

