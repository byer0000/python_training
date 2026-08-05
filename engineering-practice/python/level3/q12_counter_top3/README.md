# 問題

`collections.Counter` を使って、指定した文章の中で最も出現回数が多い単語トップ3を求めてください。

# 期待する結果

対象文章: "the quick brown fox jumps over the lazy dog the fox runs"
```python
[('the', 3), ('fox', 2), ('quick', 1)]
```
※4位以下は出現回数が同じ(1回)なので、上位2つ("the","fox")は確定、3位は実装によって
入れ替わる可能性があります（出現順で決まる仕様です）。

# ヒント

`Counter(text.split()).most_common(3)`
