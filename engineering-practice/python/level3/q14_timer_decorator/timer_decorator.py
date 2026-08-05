import time
import functools
from bank_account import BankAccount


def timer(func):
    # TODO: 実行時間を計測して表示するデコレータを実装する
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


BankAccount.withdraw = timer(BankAccount.withdraw)

if __name__ == "__main__":
    acc = BankAccount("Yuta", 1000)
    acc.withdraw(100)
