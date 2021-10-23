class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.n = len(balance)
        self.ls =balance


    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 <=self.n and account2 <=self.n and money >=0:
            if self.ls[account1-1] >= money:
                self.ls[account1-1] -=money
                self.ls[account2-1] +=money
                return True
            else:
                return False
        else:
            return False


    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.n >= account and money >=0:
            self.ls[account-1] += money
            return True
        else:
            return False


    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.n >= account and money >=0 and self.ls[account-1] >= money:
            self.ls[account-1] -=money
            return True
        else:
            return False



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)