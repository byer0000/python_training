from bank_account import BankAccount


def safe_withdraw(acc: BankAccount, amount: float) -> None:
    # TODO: try/except/finally を使って実装する
    pass


if __name__ == "__main__":
    acc = BankAccount("Yuta", 1000)
    safe_withdraw(acc, 2000)
