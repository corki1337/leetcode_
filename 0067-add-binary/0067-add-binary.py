class Solution:
    def addBinary(self, a: str, b: str) -> str:

        ans = ""
        dla = len(a)
        dlb = len(b)
        pop = 0

        if dla > dlb:
            b = ("0" * (dla - dlb)) + b
        elif dlb > dla:
            a = ("0" * (dlb- dla)) + a
        
        

        for i in range(len(a)-1, -1, -1):
            
            akt = pop + int(a[i]) + int(b[i])
            pop = 0
            if akt >=2:
                pop = 1
                akt = akt - 2
            ans += str(akt)
        if pop == 1:
            return (ans + "1")[::-1]
        return ans[::-1]
