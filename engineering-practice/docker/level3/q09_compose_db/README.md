# 問題

q08のAPIコンテナと、PostgreSQL（または任意のDB）コンテナを `docker-compose.yml` で
同時に起動できるようにしてください。APIコンテナはDBコンテナのホスト名で接続できることを確認してください。

# 期待する結果

```
$ docker-compose up -d
$ docker-compose ps
api   ... Up ... 0.0.0.0:8000->8000/tcp
db    ... Up ... 5432/tcp
```
APIコンテナ内から `db` というホスト名でPostgreSQLに接続できる。

# ヒント

Composeのネットワーク内ではサービス名がそのままホスト名になる。
