class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        minini = 10**5
        dlugosc = len(customers)
        eny = 0
        ans = 0
        for i in customers:
            if i == 'N':
                eny +=1
        
        
        minini = dlugosc - eny
        aktn = 0
        for j in range(dlugosc):
            
            if customers[j] == 'N':
                aktn += 1
            koszt = 2 * aktn + dlugosc - j - eny - 1
            
            if koszt < minini:
                minini = koszt
                ans = j + 1


        return ans