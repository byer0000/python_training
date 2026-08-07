from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0, interest_rate: float = 0.0):
        # TODO: super().__init__() を呼び出し、interest_rate を保持する
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        # TODO: balance に interest_rate分の利息を加算する
        interset = self.balance * self.interest_rate
        self.deposit(interset)

if __name__ == "__main__":
    acc = SavingsAccount("Yuta", 1000, interest_rate=0.05)
    acc.add_interest()
    print(acc.balance)  # 1050.0
