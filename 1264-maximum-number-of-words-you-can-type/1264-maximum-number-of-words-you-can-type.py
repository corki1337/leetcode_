class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        slowa = 0
        slowo = True
        for i in text:
            if i != " " and i not in brokenLetters:
                pass
            elif i in brokenLetters:
                slowo = False
            elif i == " " and slowo:
                slowa += 1
            else:
                slowo = True

        return slowa if slowo == False else slowa + 1
                

        