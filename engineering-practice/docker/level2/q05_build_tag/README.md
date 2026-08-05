# 問題

q04のイメージを `my-python-app:v1` というタグでビルドし、正しくビルドされたか
タグ一覧で確認してください。

# 期待する結果

```
$ docker images | grep my-python-app
my-python-app   v1   ...
```

# ヒント

`docker build -t`, `docker images`
