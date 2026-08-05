# 問題

`BankAccount` クラスを作成してください。属性は `owner`（所有者名）と `balance`（残高）。
メソッドとして `deposit(amount)`（入金）と `withdraw(amount)`（出金）を実装し、
残高が不足している場合は `ValueError` を送出してください。

# 期待する結果

```python
acc = BankAccount("Yuta", 1000)
acc.deposit(500)      # balance -> 1500
acc.withdraw(2000)    # ValueError: 残高不足です
```

# ヒント

`raise ValueError("残高不足です")`
