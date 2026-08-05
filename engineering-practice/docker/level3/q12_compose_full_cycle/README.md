# 問題

q09/q10のAPI＋DB構成を `docker-compose up -d` でバックグラウンド起動し、
ローカルから `curl` でヘルスチェックが通ることを確認したうえで、
`docker-compose down -v` で後片付けまで一連の流れを実行してください。

# 期待する結果

```
$ docker-compose up -d
$ curl http://localhost:8000/health
{"status":"ok"}
$ docker-compose down -v
```
`down -v` によりボリュームも含めてきれいに削除されること。

# ヒント

一連の流れをコマンド履歴として commands.sh に残しておくと後で見返しやすい。
