class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    # 入金
    def deposit(self, amount: float) -> None:
        self.balance += amount

    # 出金
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("残高不足です")
        self.balance -= amount

if __name__ == "__main__":
    acc = BankAccount("Yuta", 1000)
    acc.deposit(500)
    print(acc.balance)  # 1500
    acc.withdraw(2000)  # ValueError
