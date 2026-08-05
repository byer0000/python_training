# 問題

実行中・停止中も含め、ローカルにあるすべてのコンテナとイメージを一覧表示し、
使っていない停止済みコンテナを削除してください。

# 期待する結果

```
$ docker ps -a
$ docker container prune
Total reclaimed space: ...
```

# ヒント

`docker ps -a`, `docker images`, `docker container prune`
