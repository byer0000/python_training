# 問題

`def calc(a, b, *args, **kwargs):` という関数を定義し、`*args` に渡された数値の合計と
`**kwargs` に渡されたキーワード引数の中身を両方表示するようにしてください。
`calc(1, 2, 3, 4, mode="sum", verbose=True)` のように呼び出して確認してください。

# 期待する結果

```
args合計: 7   # 3 + 4
kwargs: {'mode': 'sum', 'verbose': True}
```

# ヒント

可変長引数の展開。`args`はタプル、`kwargs`は辞書として渡ってくる。
