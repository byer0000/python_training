# 問題

1〜30の数値のうち、3の倍数は "Fizz"、5の倍数は "Buzz"、両方の倍数は "FizzBuzz"、
それ以外は数値そのものをリストに格納してください。
for文＋if文の実装と、リスト内包表記の実装の両方を作ってください。

# 期待する結果

```
[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
 "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz"]
```
`fizzbuzz_loop()` と `fizzbuzz_comprehension()` の戻り値が一致すること。

# ヒント

`[x if 条件 else y for x in range(...)]` の形でリスト内包表記に落とし込む。
