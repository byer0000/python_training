# 問題

以下の要件を満たすDockerfileを書いてください。
- ベースイメージ: `python:3.11-slim`
- 作業ディレクトリ: `/app`
- `requirements.txt` を先にコピーして `pip install`（キャッシュを効かせる書き方）
- その後アプリ本体をコピー
- コンテナ起動時に `python main.py` を実行

# 期待する結果

```
$ docker build -t my-python-app:v1 .
$ docker run my-python-app:v1
Hello from container!
```

# ヒント

requirements.txtだけ先にCOPYしてpip installすることで、コード変更時のキャッシュが効く。
