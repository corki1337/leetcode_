class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        a = 0
        for i in num1[::-1]:
            n1 += (ord(i)-48) * 10 ** a
            a += 1
        a = 0
        for i in num2[::-1]:
            n2 += (ord(i)-48) * 10 ** a
            a += 1
        
        n3 = n1 * n2

        return str(n3)