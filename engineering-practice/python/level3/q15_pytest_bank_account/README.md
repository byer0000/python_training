# 問題

`pytest` を使って、`BankAccount` クラスに対するテストコード `test_bank_account.py` を
書いてください。最低でも「正常な入金」「残高不足での出金がエラーになること」の2パターンをテストしてください。

# 期待する結果

```
$ pytest
====== 2 passed in 0.01s ======
```

# ヒント

`pytest.raises(ValueError)` を使うと例外の発生をテストできる。
