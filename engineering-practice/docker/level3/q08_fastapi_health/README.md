# 問題

FastAPI（またはFlask）で `/health` エンドポイントが `{"status": "ok"}` を返すだけのAPIを
作り、Dockerfileでコンテナ化してください。ポート8000番をホストに公開してください。

# 期待する結果

```
$ docker run -p 8000:8000 health-api
$ curl http://localhost:8000/health
{"status":"ok"}
```

# ヒント

`EXPOSE 8000`, `docker run -p 8000:8000`
