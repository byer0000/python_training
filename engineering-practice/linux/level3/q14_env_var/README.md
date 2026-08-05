# 問題

環境変数 `APP_ENV` を `production` に設定し、Pythonスクリプトからその値を読み取って
表示するコードを書いてください。

# 期待する結果

```
$ export APP_ENV=production
$ python3 env_demo.py
現在の環境: production
```

# ヒント

`export`, Pythonの `os.environ.get()`
