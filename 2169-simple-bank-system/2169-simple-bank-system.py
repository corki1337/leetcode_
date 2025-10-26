class Bank:
    
    
    
    

    def __init__(self, balance: List[int]):
        self.balans = []
        for i in balance:
            self.balans.append(i)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balans) or account2 > len(self.balans):
            return False


        if self.balans[account1 -1] < money:
            return False
        else:
            self.balans[account1 -1] -= money
            self.balans[account2 -1] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balans):
            return False
        else:
            self.balans[account -1] += money
            return True





    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balans):
            return False
        elif self.balans[account - 1] < money:
            return False
        else:
            self.balans[account - 1] -= money
            return True
        
        




# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)