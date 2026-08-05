# 問題

`BankAccount` を継承した `SavingsAccount` クラスを作り、`interest_rate`（利率）属性を追加。
`add_interest()` メソッドで利息を残高に加算する処理を実装してください。

# 期待する結果

```python
acc = SavingsAccount("Yuta", 1000, interest_rate=0.05)
acc.add_interest()
print(acc.balance)  # 1050.0
```

# ヒント

`class SavingsAccount(BankAccount):` / `super().__init__(owner, balance)`
