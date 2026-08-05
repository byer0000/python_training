# 問題

マルチステージビルドを使い、ビルド用ステージと実行用ステージを分けたDockerfileに
書き換えてください。最終イメージが軽量化されることを確認してください。

# 期待する結果

```
$ docker build -t my-python-app:multistage .
$ docker images
```
シングルステージ版よりイメージサイズが小さくなっている。

# ヒント

`FROM ... AS builder`, `COPY --from=builder`
