# 問題

`docker-compose.yml` に環境変数ファイル（`.env`）を読み込ませ、DBのパスワード等を
ハードコードせずに渡せるようにしてください。

# 期待する結果

```
$ docker-compose up -d
```
`.env` に書いた `DB_PASSWORD` の値が、コンテナ内の環境変数として反映されている。

# ヒント

`env_file:`, `${VAR_NAME}` 構文
