# 問題

`python:3.11-slim` の代わりに `python:3.11-alpine` を使ったDockerfileも作り、
イメージサイズを比較してください。alpineで依存関係のインストールに失敗する場合はその原因も調べてください。

# 期待する結果

```
$ docker images
my-python-app-slim     ...   150MB
my-python-app-alpine   ...   55MB
```
（数値は環境により変動。alpineは musl libc ベースでビルドツール不足によりコンパイルが必要な
パッケージのインストールに失敗しやすい点を確認する）

# ヒント

alpineでは `apk add build-base` 等が必要になる場合がある。
