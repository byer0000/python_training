# 問題

Docker演習で作成したDockerfileをこのリポジトリに組み込み、CI上で `docker build` が
通ることを確認するステップを追加してください。

# 期待する結果

Actionsのログで `docker build` が成功したことが確認できる。

# ヒント

`docker build -t test-image .`
