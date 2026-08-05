# 問題

`../../sample_app/` の `add()` 関数のテストが、CI上で自動実行されるようにしてください。
わざとテストを失敗させて、CIが赤くなる(failする)ことも確認してください。

# 期待する結果

```
$ pytest sample_app/
1 passed in 0.01s
```
（`add`の実装を壊すと `1 failed` になりCIが赤くなる）

# ヒント

`run: pytest sample_app/`
