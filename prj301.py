class Bank:
    
    def __init__(self,am=0.00):
        self.__Amount = am
        self.na = self.__Amount
        while True:
            self.word = input("1 for Withdraw or 2 for Deposit or q to quit: ")

            if self.word == "1":
                self.wd()
            elif self.word == "2":
                self.de()
            elif self.word == "q":
                break
            else:
                print("Invalid Input")

    def log_t(self,n):
        with open("prj301.txt", "a") as f:
            f.write(n)
    def wd(self):
        try:
            us = int(input("Enter Amount To Withdraw: "))
            if self.__Amount > us:
                self.__Amount = self.__Amount - us
                print("Withdrawal successful. Remaining balance:", self.__Amount)
                self.na = self.__Amount
            else:
                print("Insufficient Balance: ", self.na)

            self.log_t(self.na)
        except:
            print("Invalid Input")
            

    def de(self):
        try:
            us = int(input("Enter Amount To Deposit: "))
            self.__Amount = self.__Amount + us
            self.na = self.__Amount
            print("Deposit successful. Updated balance:", self.__Amount)
            self.log_t(self.na)
        except:
            print("Invalid Input")


afi = Bank(100)

