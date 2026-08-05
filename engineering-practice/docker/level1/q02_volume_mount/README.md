# 問題

`hello.py`（同じフォルダに用意済み）をボリュームマウントでコンテナに渡して実行してください
（イメージをビルドせずに）。

# 期待する結果

```
$ docker run -v $(pwd):/app -w /app python:3.11-slim python hello.py
Hello from Docker
```

# ヒント

`-v ホスト:コンテナ`, `-w`(作業ディレクトリ指定)
